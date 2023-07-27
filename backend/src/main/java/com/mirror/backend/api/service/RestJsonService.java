package com.mirror.backend.api.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Service
public class RestJsonService {

    private final String REDIRECT_URI= "http://localhost:8080/schedule";
    private final String GRANT_TYPE= "authorization_code";
    private final String TOKEN_URL = "https://oauth2.googleapis.com/token";

    public RestJsonService() {}

    public String getAccessTokenJsonData(String code, String CLIENT_ID, String CLIENT_SECRET) throws JsonProcessingException {
        RestTemplate restTemplate = new RestTemplate();

        Map<String, Object> params = new HashMap<>();
        params.put("code", code);
        params.put("client_id", CLIENT_ID);
        params.put("client_secret", CLIENT_SECRET);
        params.put("redirect_uri", REDIRECT_URI);
        params.put("grant_type", GRANT_TYPE);

        ResponseEntity<String> responseEntity =
                restTemplate.postForEntity(TOKEN_URL, params, String.class); // POST 방식으로 전송
        
        String json = responseEntity.getBody();
        return json;
    }
}
