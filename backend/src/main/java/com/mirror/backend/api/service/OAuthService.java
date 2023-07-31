package com.mirror.backend.api.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.dto.GoogleOAuthResponseDto;
import com.mirror.backend.api.dto.ResponseLogin;
import com.mirror.backend.api.entity.RedisUserToken;
import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import com.mirror.backend.api.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

@Service
public class OAuthService {

    static int FAIL = 0;
    static int SUCCESS = 1;
    static int RE_LOGIN_USER = 0;
    static int INIT_LOGIN_USER = 1;

    @Autowired
    private UserRepository userRepository;
    @Autowired
    private RedisUserTokenRepository redisUserTokenRepository;
    @Autowired
    private GoogleOAuth googleOAuth;
    @Autowired
    private UserService userService;

    private ResponseLogin responseLogin;
    private GoogleOAuthResponseDto googleOAuthResponseDto ;


    public String getRequestUrlForAuthorizationCode() throws UnsupportedEncodingException {
        String endPoint = googleOAuth.REQUEST_AUTH_CODE_URL;

        String redirectUri = googleOAuth.getRedirectUri();
        String clientId = googleOAuth.getClientId();
        String responseType = "code";
        String scopeCalendar = googleOAuth.SCOPE_CALENDAR;
        String scopeTask = googleOAuth.SCOPE_TASK;

        StringBuilder requestUrl = new StringBuilder();
        requestUrl.append(endPoint)
                .append("?client_id=").append(clientId)
                .append("&redirect_uri=").append(redirectUri)
                .append("&response_type=").append(responseType)
                .append("&scope=")
                .append(URLEncoder.encode(scopeCalendar + " ", "UTF-8"))
                .append(URLEncoder.encode(scopeTask + " ", "UTF-8"))
                .append("email+")
                .append("profile")
                .append("&access_type=").append("offline"); //TODO: remove this Line (RefreshToken받으려고 함)
//                .append("&prompt=").append("consent");

        System.out.println(requestUrl.toString());
        return requestUrl.toString();
    }

    public ResponseLogin login (String authCode){
        googleOAuthResponseDto = new GoogleOAuthResponseDto();

        // 1. authCode를 Access/Refresh/Id Token으로 변환하여 지역변수로 저장
        saveGoogleTokens(authCode);

        // 2. idToken을 이용하여 GoogleOAuth 로그인한 user의 googleEmail찾기
        String userEmail = getUserEmailFromIdToken();

        // 3. 해당 Email이 MariaDB에 존재하는 값인지 확인
        boolean isExistUser = userService.isExistUser(userEmail);

        responseLogin = new ResponseLogin();
        // 존재유무에따라, Front에게 추가기입 창을 안내하라는 Signal(0, 1) 설정
        if ( !isExistUser){
            // 최초의 유저 정보 생성
            userService.createUser(userEmail);
            responseLogin.setIsInitLoginUser(INIT_LOGIN_USER);
        }else{
            responseLogin.setIsInitLoginUser(RE_LOGIN_USER);
        }

         // 4. userEmail을 Key으로 하여 Access/Refresh Token을 Redis에 저장
        saveUserTokenToRedis(userEmail);
//        System.out.println("Redis에 Token저장 완료");

        responseLogin.setAccessToken(googleOAuthResponseDto.getAccessToken());
        responseLogin.setRefreshToken(googleOAuthResponseDto.getRefreshToken());

        return responseLogin;
    }

    public void saveUserTokenToRedis(String userEmail){
        String key = "token_" + userEmail;

        RedisUserToken send = new RedisUserToken(key,
                googleOAuthResponseDto.getAccessToken(),
                googleOAuthResponseDto.getRefreshToken());

        redisUserTokenRepository.save(send);

//        System.out.println("유저 token정보 저장");
    }


    public String getUserEmailFromIdToken(){

        String userEmail = "";
        String[] parts = googleOAuthResponseDto.getIdToken().split("\\."); // '.'을 기준으로 분리

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

    public void saveGoogleTokens(String authCode) {
        // 승인코드로 access, refresh 토큰으로 교환하기
        ObjectMapper mapper = new ObjectMapper();

        String endPoint = googleOAuth.REQUEST_TOKEN_URL;

        String clientId = googleOAuth.getClientId();
        String clientSecret = googleOAuth.getClientSecret();
        String code = authCode;
        String grantType = "authorization_code";
        String redirectUri = googleOAuth.getRedirectUri();

        RestTemplate restTemplate = new RestTemplate();

        MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
        map.add("client_id", clientId);
        map.add("client_secret", clientSecret);
        map.add("code", code);
        map.add("grant_type", grantType);
        map.add("redirect_uri", redirectUri);

        // 응답받기
        ResponseEntity<String> responseEntity= null ;
        JsonNode returnNode = null;
        try {
            responseEntity = restTemplate.postForEntity(endPoint, map, String.class);
            returnNode = mapper.readTree(responseEntity.getBody());
        } catch (IOException e) {
            e.printStackTrace();
        }

        // AccessToken, expiresIn, refreshToken, scope, tokenType, idToken 확인
         System.out.println("responseEntity: " + responseEntity.toString());

        googleOAuthResponseDto.setAccessToken(returnNode.get("access_token").asText());
        googleOAuthResponseDto.setRefreshToken(returnNode.get("refresh_token").asText());
        googleOAuthResponseDto.setIdToken(returnNode.get("id_token").asText());


    }



    public int getUserEmailfromAccessToken() {

        String endPoint = googleOAuth.REQUEST_USER_INFO_URL;

        // RestTemplate로 GET요청 보내기
        RestTemplate restTemplate = new RestTemplate();
        ObjectMapper mapper = new ObjectMapper();

        // header설정, accessToken담기
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.set("Authorization", "Bearer " + googleOAuthResponseDto.getAccessToken());
        HttpEntity<String> entity = new HttpEntity<>("parameters", headers);

        // 응답받기
        ResponseEntity<String> response = null;
        JsonNode returnNode = null;
        try {
            response = restTemplate.exchange(endPoint, HttpMethod.GET, entity, String.class);
            System.out.println("\nSending 'GET' request to URL : " + endPoint);
            System.out.println("Response Code : " + response.getStatusCodeValue());

            returnNode = mapper.readTree(response.getBody());
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println(returnNode);
        System.out.println(returnNode.get("email").asText());

        return SUCCESS;
    }

}

