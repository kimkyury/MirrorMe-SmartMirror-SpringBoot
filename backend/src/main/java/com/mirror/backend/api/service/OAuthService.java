package com.mirror.backend.api.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.dto.ResponseGoogleOAuthDto;
import com.mirror.backend.api.dto.ResponseLoginDto;
import com.mirror.backend.api.dto.ResponseTokensDto;
import com.mirror.backend.api.entity.RedisUserToken;
import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Optional;

@Service
public class OAuthService {

    private GoogleOAuth googleOAuth;
    private RedisUserTokenRepository redisUserTokenRepository;
    private UserService userService;

    @Autowired
    public OAuthService(GoogleOAuth googleOAuth, RedisUserTokenRepository redisUserTokenRepository, UserService userService) {
        this.googleOAuth = googleOAuth;
        this.redisUserTokenRepository = redisUserTokenRepository;
        this.userService = userService;
    }


    private ResponseLoginDto responseLogin;
    private ResponseGoogleOAuthDto googleOAuthResponseDto ;

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
                .append("&access_type=").append("offline"); //TODO: remove this Line (RefreshToken받으려고 함)
//                .append("&prompt=").append("consent");

        System.out.println(requestUrl.toString());
        return requestUrl.toString();
    }

    public ResponseLoginDto login(String authCode){

        googleOAuthResponseDto = new ResponseGoogleOAuthDto();

         int RE_LOGIN_USER = 0;
         int INIT_LOGIN_USER = 1;

         // 1. authCode를 Access/Refresh/Id Token으로 변환하여 지역변수로 저장
        saveGoogleTokens(authCode);

        // 2. idToken을 이용하여 GoogleOAuth 로그인한 user의 googleEmail찾기
        String userEmail = getUserEmailFromIdToken();

        // 3. 해당 Email이 MariaDB에 존재하는 값인지 확인
        boolean isExistUser = userService.isExistUser(userEmail);

        responseLogin = new ResponseLoginDto();
        // 존재유무에따라, Front에게 추가기입 창을 안내하라는 Signal(0, 1) 설정
        if (!isExistUser){
            // 최초의 유저 정보 생성
            userService.createUser(userEmail);
            responseLogin.setIsInitLoginUser(INIT_LOGIN_USER);
        }else{
            responseLogin.setIsInitLoginUser(RE_LOGIN_USER);
        }

         // 4. userEmail을 Key으로 하여 Access/Refresh Token을 Redis에 저장
        saveUserTokenToRedis(userEmail);

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

    public ResponseTokensDto getTokensFromUserEmail(String userEmail) {
        // :TODO 등록되지 않은 유저의 Email로 요청시 예외처리
        String key = "token_" + userEmail;
        Optional<RedisUserToken> redisUserTokenOptional = redisUserTokenRepository.findById(key);

        if ( redisUserTokenOptional.isEmpty()){
            return null;
        }

        RedisUserToken redisUserToken = redisUserTokenOptional.get();

        ResponseTokensDto tokenDto = ResponseTokensDto.builder()
                .accessToken(redisUserToken.getAccessToken())
                .refreshToken(redisUserToken.getRefreshToken())
                .build();

        return tokenDto;
    }
}

