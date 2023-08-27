package com.mirror.backend.api.service.impl;


import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.dto.*;
import com.mirror.backend.api.entity.GoogleOAuthToken;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.repository.GoogleOAuthTokenRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.UserService;
import com.mirror.backend.common.utils.Constants.Result;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestTemplate;
import springfox.documentation.service.OAuth;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.NoSuchElementException;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class OAuthServiceImpl implements OAuthService {

    private final GoogleOAuth googleOAuth;
    private final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    private final UserService userService;
    private final UserRepository userRepository;

    private GoogleOAuthDto.GoogleOAuthRes googleOAuthResponseDto;

    public String getRequestUrlForAuthorizationCode() throws UnsupportedEncodingException {
        String endPoint = GoogleOAuth.REQUEST_AUTH_CODE_URL;
        String redirectUri = googleOAuth.getRedirectUri();
        String clientId = googleOAuth.getClientId();
        String responseType = "code";
        String scopeCalendar = GoogleOAuth.SCOPE_CALENDAR;
        String scopeTask = GoogleOAuth.SCOPE_TASK;

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
                .append("&access_type=").append("offline") //TODO: remove this Line (RefreshToken받으려고 함)
                .append("&prompt=").append("consent");

        System.out.println(requestUrl.toString());
        return requestUrl.toString();
    }

    public void oAuthGoogleLogin(String authCode){

        googleOAuthResponseDto = new GoogleOAuthDto.GoogleOAuthRes();

        saveGoogleTokens(authCode);

        String userEmail = getUserEmailFromIdToken();
        boolean isExistUser = userService.isExistUser(userEmail);
        if (!isExistUser) userService.createUser(userEmail);

        saveUserTokenToRedis(userEmail);
    }

    public void saveUserTokenToRedis(String userEmail){
        String key = userEmail;

        GoogleOAuthToken send = new GoogleOAuthToken(key,
                googleOAuthResponseDto.getAccessToken(),
                googleOAuthResponseDto.getRefreshToken());

        googleOAuthTokenRepository.save(send);
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
        return userEmail;
    }

    public void saveGoogleTokens(String authCode) {
        // 승인코드로 access, refresh 토큰으로 교환하기
        ObjectMapper mapper = new ObjectMapper();

        String endPoint = GoogleOAuth.REQUEST_TOKEN_URL;
        String clientId = googleOAuth.getClientId();
        String clientSecret = googleOAuth.getClientSecret();
        String code = authCode;
        String grantType = "authorization_code";
        String redirectUri = googleOAuth.getRedirectUri();

        MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
        map.add("client_id", clientId);
        map.add("client_secret", clientSecret);
        map.add("code", code);
        map.add("grant_type", grantType);
        map.add("redirect_uri", redirectUri);

        // 응답받기
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity= null ;
        JsonNode returnNode = null;
        try {
            responseEntity = restTemplate.postForEntity(endPoint, map, String.class);
            returnNode = mapper.readTree(responseEntity.getBody());
        } catch (IOException e) {
            e.printStackTrace();
        }

        googleOAuthResponseDto.setAccessToken(returnNode.get("access_token").asText());
        googleOAuthResponseDto.setRefreshToken(returnNode.get("refresh_token").asText());
        googleOAuthResponseDto.setIdToken(returnNode.get("id_token").asText());
    }

    public TokensDto.TokensRes getTokensFromUserEmail(String userEmail) {

        GoogleOAuthToken googleOAuthToken = googleOAuthTokenRepository.findById(userEmail).orElseThrow(
                () -> new NoSuchElementException("해당 Email은 존재하지 않습니다.")
        );

        TokensDto.TokensRes tokensRes = TokensDto.TokensRes.builder()
                .accessToken(googleOAuthToken.getAccessToken())
                .refreshToken(googleOAuthToken.getRefreshToken())
                .build();

        return tokensRes;
    }

    public String getUserEmailFromAccessToken(String accessToken){
        RestTemplate restTemplate = new RestTemplate();
        StringBuilder googleRequestURL = new StringBuilder();
        googleRequestURL.append("https://www.googleapis.com/oauth2/v1/tokeninfo")
                .append("?access_token=").append(accessToken);

        ObjectMapper mapper = new ObjectMapper();

        ResponseEntity<String> responseEntity = null;
        JsonNode returnNode = null;
        String userEmail = "";

        try {
            responseEntity = restTemplate.getForEntity(googleRequestURL.toString(), String.class);
            returnNode = mapper.readTree(responseEntity.getBody());
            userEmail = returnNode.get("email").asText();
        }catch (HttpClientErrorException e){
            e.getStackTrace();
        } catch (JsonMappingException e) {
            e.printStackTrace();
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        return userEmail;
    }

    public int saveUserPassword(UserDto.UserSavePasswordReq userSavePasswordReq) {

        String userEmail = userSavePasswordReq.getUserEmail();
        String password = userSavePasswordReq.getPassword();

        //TODO: password 암호화

        Optional<User> user = userRepository.findByUserEmail(userEmail);
        user.ifPresent( selectUser -> {
            selectUser.setPassword(password);
            userRepository.save(selectUser);
        });

        return Result.SUCCESS;
    }

    public LoginDto.LoginRes confirmLogin(LoginDto.LoginReq loginReq) {

        String inputUserEmail = loginReq.getUserEmail();
        String inputPassword = loginReq.getPassword();
        User dbUser = userRepository.findByUserEmail(inputUserEmail)
                .orElseThrow( () -> new NoSuchElementException("해당 Email은 존재하지 않습니다. "));

        if ( !inputPassword.equals(dbUser.getPassword()))
            return null; // 유저는 존재하지만, 패스워드가 일치하지 않음

        int isInitLoginUser = -1;
        if (dbUser.getUserName() == null)
            isInitLoginUser = 1;
        else
            isInitLoginUser = 0;

        GoogleOAuthToken googleOAuthToken = googleOAuthTokenRepository.findById(inputUserEmail)
                .orElseThrow( () -> new NoSuchElementException());

        LoginDto.LoginRes loginRes = LoginDto.LoginRes.builder()
                .isInitLoginUser(isInitLoginUser)
                .accessToken(googleOAuthToken.getAccessToken())
                .refreshToken(googleOAuthToken.getRefreshToken())
                .build();

        return loginRes;
    }
}

