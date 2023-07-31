package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class GoogleOauthResponseDto {

    private String accessToken;
    private String expiresIn;
    private String refreshToken;
    private String scope;
    private String tokenType;
    private String idToken;
}
