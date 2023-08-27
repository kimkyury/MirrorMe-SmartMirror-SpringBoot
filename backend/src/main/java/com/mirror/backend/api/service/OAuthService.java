package com.mirror.backend.api.service;

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
import com.mirror.backend.common.utils.Constants.Result;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.NoSuchElementException;
import java.util.Optional;


public interface OAuthService {

    public String getRequestUrlForAuthorizationCode() throws UnsupportedEncodingException;

    public void oAuthGoogleLogin(String authCode);

    public LoginDto.LoginRes confirmLogin(LoginDto.LoginReq loginReq);

    public TokensDto.TokensRes getTokensFromUserEmail(String userEmail);

    public String getUserEmailFromAccessToken(String accessToken);

    public int saveUserPassword(UserDto.UserSavePasswordReq userSavePasswordReq);


    // --- Unused Method
    public void saveUserTokenToRedis(String userEmail);
    public String getUserEmailFromIdToken();
    public void saveGoogleTokens(String authCode);
}

