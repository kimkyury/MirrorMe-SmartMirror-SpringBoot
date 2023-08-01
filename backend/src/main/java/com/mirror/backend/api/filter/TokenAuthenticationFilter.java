package com.mirror.backend.api.filter;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.entity.RedisUserToken;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import com.mirror.backend.api.repository.UserRepository;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.context.WebApplicationContext;
import org.springframework.web.context.support.WebApplicationContextUtils;

import javax.servlet.*;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Optional;

@Component
public class TokenAuthenticationFilter implements Filter {


    private RedisUserTokenRepository redisUserTokenRepository;
    private UserRepository userRepository;
    private GoogleOAuth googleOAuth;

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        ServletContext servletContext = filterConfig.getServletContext();
        WebApplicationContext webApplicationContext = WebApplicationContextUtils.getWebApplicationContext(servletContext);

        redisUserTokenRepository = webApplicationContext.getBean(RedisUserTokenRepository.class);
        googleOAuth = webApplicationContext.getBean(GoogleOAuth.class);
        userRepository = webApplicationContext.getBean(UserRepository.class);
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {

        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;

        // Header에서 AccessToken 가져옴
        String accessToken = request.getHeader("access_token");

        // Google Oauth에 AccessToken 유효성 검사 요청
        RestTemplate restTemplate = new RestTemplate();
        StringBuilder googleRequestURL = new StringBuilder();
        googleRequestURL.append("https://www.googleapis.com/oauth2/v1/tokeninfo")
            .append("?access_token=").append(accessToken);

        ResponseEntity<String> responseEntity = null;
        JsonNode returnNode = null;
        ObjectMapper mapper = new ObjectMapper();

        String userEmail = "";
        Long userId;

        try {
            responseEntity = restTemplate.getForEntity(googleRequestURL.toString(), String.class);
            returnNode = mapper.readTree(responseEntity.getBody());

            userEmail = returnNode.get("email").asText();
            userId = getUserIdFromUserEmail(userEmail);

            servletRequest.setAttribute("user_email", userEmail);
            servletRequest.setAttribute("user_id", userId);

            filterChain.doFilter(servletRequest, servletResponse); // AccessToken이 유효하다면 다음 Filter 또는 Controller로 요청 전달
        } catch (HttpClientErrorException e) {
            if (e.getStatusCode() == HttpStatus.BAD_REQUEST) {
                System.out.println("--------Filter-------");
                System.out.println("해당 AccessToken이 유효하지 않으므로 Cookie내용을 따라 재발급합니다.");
                // AccessToken이 유효하지 않다면 클라이언트에 401 Unauthorized 응답

                // refreshToken으로 새 accessToken 재발급
                Cookie[] cookies = request.getCookies();
                String refreshToken = null;
                for (Cookie cookie : cookies) {
                    if (cookie.getName().equals("refresh_token")) {
                        refreshToken = cookie.getValue();
                        break;
                    }
                }

                if (refreshToken != null) {
                    String[] tokens =  reissueToken(refreshToken); // 0: accessToken, 1:id_token
                    String reIssueAccessToken = tokens[0];
                    String idToken = tokens[1];

                    userEmail = getUserEmailFromIdToken(idToken);
                    saveAccessTokenToRedis(userEmail, reIssueAccessToken, refreshToken);

//                    System.out.println("userEmail: " + userEmail);
                    System.out.println("AccessToken: " + accessToken);
                    System.out.println("reIssueAccessToken: " + reIssueAccessToken);
                    System.out.println("RefreshToken: " + refreshToken);

                    // 클라이언트에게 새로 발급 받은 accessToken과 refreshToken을 JSON 형태로 응답합니다.
                    response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
                    response.setContentType("application/json");
                    PrintWriter out = response.getWriter();
                    out.print("{\"access_token\":\"" + reIssueAccessToken + "\",\"refresh_token\":\"" + refreshToken + "\"}");
                    out.flush();
                } else {
                    // refreshToken이 존재하지 않는 경우, Unauthorized 응답을 전송합니다.
                    response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
                    response.getWriter().write("Invalid access token");
                }
            } else {
                throw e; // 다른 문제가 발생했다면 예외를 던짐
            }
        }

    }

    private Long getUserIdFromUserEmail(String userEmail){
        Optional< User > user = userRepository.findByUserEmail(userEmail);
        Long userId = user.get().getUserId();
        return userId;
    }


    private String[] reissueToken(String refreshToken){

        RestTemplate restTemplate = new RestTemplate();

        MultiValueMap<String, String> parameters = new LinkedMultiValueMap<>();
        parameters.add("client_id", googleOAuth.getClientId());
        parameters.add("client_secret", googleOAuth.getClientSecret());
        parameters.add("refresh_token", refreshToken);
        parameters.add("grant_type", "refresh_token");

        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Type", "application/x-www-form-urlencoded");

        HttpEntity<MultiValueMap<String, String>> request = new HttpEntity<>(parameters, headers);

        ObjectMapper mapper = new ObjectMapper();
        ResponseEntity<String> response = null;
        JsonNode returnNode = null;

        String accessToken = "";
        String id_token = "";
        try {
            response = restTemplate.postForEntity("https://oauth2.googleapis.com/token", request, String.class);
            returnNode = mapper.readTree(response.getBody());
        } catch (IOException e) {
            e.printStackTrace();
        }

         accessToken = returnNode.get("access_token").asText();
         id_token = returnNode.get("id_token").asText();

         String [] tokens = new String[2];
         tokens[0] = accessToken;
         tokens[1] = id_token;

        return tokens;
    }



    public String getUserEmailFromIdToken (String idToken ){

        String userEmail = "";
        String[] parts = idToken.split("\\."); // '.'을 기준으로 분리

        if (parts.length == 3) {

            // payload영역만 Decode 후, Jackson으로 userEmail부분만 Parsing
            byte[] payloadBytes = Base64.getUrlDecoder().decode(parts[1]);
            String payload = new String(payloadBytes, StandardCharsets.UTF_8);

            try {
                ObjectMapper objectMapper = new ObjectMapper();
                JsonNode payloadNode = objectMapper.readTree(payload);
                if (payloadNode.has("email")) {
                    userEmail = payloadNode.get("email").asText();

                } else {
                    System.out.println("Email not found.");
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            System.out.println("Invalid ID token.");
        }
//        System.out.println("User의 Email: " + userEmail);
        return userEmail;
    }

    private void saveAccessTokenToRedis( String userEmail, String accessToken ,String refreshToken){
        String key = "token_" + userEmail;

        RedisUserToken send = new RedisUserToken(key,
                accessToken,
                refreshToken);

        redisUserTokenRepository.save(send);
    }


    @Override
    public void destroy() {

    }
}