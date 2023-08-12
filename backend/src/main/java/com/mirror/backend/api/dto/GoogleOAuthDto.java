package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

public class GoogleOAuthDto {

    @Getter
    @Setter
    @ToString
    public static class GoogleOAuthRes{
        private String accessToken;
        private String expiresIn;
        private String refreshToken;
        private String scope;
        private String tokenType;
        private String idToken;
    }
}
