package com.mirror.backend.api.info;

import lombok.Getter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;


@Getter
@Component
public class GoogleOAuth {

    private final String googleLoginUrl = "https://accounts.google.com";
    private final String googleEndPoint = "https://accounts.google.com/o/oauth2/v2/auth";
    private final String GOOGLE_TOKEN_REQUEST_URL = "";
    private final String GOOGLE_USERINFO_REQUEST_URL = "";

    @Value("${google.client-id}")
    private String googleClientId;

//    @Value("${google.redirect-uri-oauth}")
    private String googleRedirectUriOauth;

//    @Value("${google.redirect-uri-token}")
    private String googleRedirectUriToken;

//    @Value("${google.redirect-uri-code}")
    private String googleRedirectUriCode;


    @Value("${google.client-secret}")
    private String googleClientSecret;

}
