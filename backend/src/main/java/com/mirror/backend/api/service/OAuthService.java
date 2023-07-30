package com.mirror.backend.api.service;

import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import com.mirror.backend.api.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.server.ResponseStatusException;

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
                .append("email ")
                .append("profile");

        System.out.println(requestUrl.toString());
        return requestUrl.toString();

    }


    public int getGoogleToken(String authCode) {
        // 승인코드로 access, refresh 토큰으로 교환하기
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
        if (responseEntity.getStatusCode() == HttpStatus.OK)
            return FAIL;
        return SUCCESS;
    }


}

