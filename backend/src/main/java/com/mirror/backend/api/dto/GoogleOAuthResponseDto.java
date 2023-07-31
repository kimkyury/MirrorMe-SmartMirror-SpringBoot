package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class GoogleOAuthResponseDto {

    private String accessToken;
    private String expiresIn;
    private String refreshToken;
    private String scope;
    private String tokenType;
    private String idToken;


    @Override
    public String toString() {
        return "GoogleOAuthResponseDto{" +
                "accessToken='" + accessToken + '\'' +
                ", expiresIn='" + expiresIn + '\'' +
                ", refreshToken='" + refreshToken + '\'' +
                ", scope='" + scope + '\'' +
                ", tokenType='" + tokenType + '\'' +
                ", idToken='" + idToken + '\'' +
                '}';
    }
}
