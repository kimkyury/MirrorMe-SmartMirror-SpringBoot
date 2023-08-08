package com.mirror.backend.common.utils;


import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.entity.RedisUserToken;
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
import java.io.IOException;


@Component
public class TokenUtil {


    private RedisUserTokenRepository redisUserTokenRepository;
    private UserRepository userRepository;
    private GoogleOAuth googleOAuth;


    public TokenUtil(RedisUserTokenRepository redisUserTokenRepository, UserRepository userRepository, GoogleOAuth googleOAuth) {
        this.redisUserTokenRepository = redisUserTokenRepository;
        this.userRepository = userRepository;
        this.googleOAuth = googleOAuth;
    }



    public  String confirmAccessToken(String accessToken, String refreshToken)  {


        // Google Oauth에 AccessToken 유효성 검사 요청
        RestTemplate restTemplate = new RestTemplate();
        StringBuilder googleRequestURL = new StringBuilder();
        googleRequestURL.append("https://www.googleapis.com/oauth2/v1/tokeninfo")
                .append("?access_token=").append(accessToken);

        ObjectMapper mapper = new ObjectMapper();

        ResponseEntity<String> responseEntity = null;
        JsonNode returnNode = null;

        String userEmail = "";
        Long userId;


        try{
            responseEntity = restTemplate.getForEntity(googleRequestURL.toString(), String.class);

            try {
                returnNode = mapper.readTree(responseEntity.getBody());
            }catch(IOException e){
                e.fillInStackTrace();
            }
            userEmail = returnNode.get("email").asText();
        }catch(HttpClientErrorException e) {
            if (e.getStatusCode() == HttpStatus.BAD_REQUEST) {
                System.out.println("--------Filter-------");
                System.out.println("해당 AccessToken이 유효하지 않으므로 refreshToken을 통해 재발급합니다. ");

                // refreshToken으로 새 accessToken 재발급
                String [] tokens = reIssueAccessToken(refreshToken);
                String reIssueAccessToken = tokens[0];

                saveTokensToRedis(userEmail, reIssueAccessToken, refreshToken);
                return reIssueAccessToken;
            }
        }

        return accessToken;
    }


    public  String [] reIssueAccessToken(String refreshToken){
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

    public  void saveTokensToRedis(String userEmail, String reIssueAccessToken, String refreshToken){
        RedisUserToken reIssueToken = new RedisUserToken(userEmail,
                reIssueAccessToken,
                refreshToken);

        redisUserTokenRepository.save(reIssueToken);
    }
}
