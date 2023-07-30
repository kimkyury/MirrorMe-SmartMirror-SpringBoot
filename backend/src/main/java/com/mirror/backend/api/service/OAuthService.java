package com.mirror.backend.api.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import com.mirror.backend.api.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.server.ResponseStatusException;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

@Service
public class OAuthService {

    static int FAIL = 0;
    static int SUCCESS = 1;

    @Autowired
    private UserRepository userRepository;
    @Autowired
    private RedisUserTokenRepository redisUserTokenRepository;
    @Autowired
    private GoogleOAuth googleOAuth;

    private String accessToken;
    private String refreshToken;

    public User getUser(Long userId) {
        return userRepository.findById(userId)
                .orElseThrow(() ->
                        new ResponseStatusException(HttpStatus.NOT_FOUND, "User not found"));
    }


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


    public int getGoogleToken(String authCode) throws JsonProcessingException {
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

        ResponseEntity<String> responseEntity =
                restTemplate.postForEntity(endPoint, map, String.class);

        System.out.println("responseEntity: " + responseEntity.toString());

        JsonNode returnNode = mapper.readTree(responseEntity.getBody());
        accessToken = returnNode.get("access_token").asText();
        refreshToken = returnNode.get("id_token").asText();

        // id_token 디코딩 후, email을 key로 하는 redis Data생성  ( value: refresh, access)


        if (responseEntity.getStatusCode() != HttpStatus.OK)
            return FAIL;
        return SUCCESS;
    }

    public int getUserEmail() {

        String endPoint = googleOAuth.REQUEST_USER_INFO_URL;

        // RestTemplate로 GET요청 보내기
        RestTemplate restTemplate = new RestTemplate();
        ObjectMapper mapper = new ObjectMapper();

        // header설정, accessToken담기
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.set("Authorization", "Bearer " + accessToken);
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

