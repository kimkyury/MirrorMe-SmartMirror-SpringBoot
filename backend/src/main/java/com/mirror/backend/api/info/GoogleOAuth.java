package com.mirror.backend.api.info;

import lombok.Getter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;


@Getter
@Component
public class GoogleOAuth {


    public final String REQUEST_AUTH_CODE_URL = "https://accounts.google.com/o/oauth2/v2/auth";
    // 갱신시: POST
    public final String REQUEST_TOKEN_URL = "https://oauth2.googleapis.com/token";

    public final String SCOPE_CALENDAR = "https://www.googleapis.com/auth/calendar.events.readonly";
    public final String SCOPE_TASK = "https://www.googleapis.com/auth/tasks.readonly";


    @Value("${google.client-id}")
    private String clientId;
    @Value("${google.client-secret}")
    private String clientSecret;


    // receive AuthorizationCode
    @Value("${google.redirect-uri}")
    private String redirectUri;

    // receive Authorization Access/Refresh Token
//    @Value("${google.redirect-uri-token}")
//    private String redirectUriToken;


}
