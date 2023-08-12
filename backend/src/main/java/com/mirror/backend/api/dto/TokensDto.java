package com.mirror.backend.api.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

public class TokensDto {

    @Getter
    @ToString
    public static class TokensRes{
        private String accessToken;
        private String refreshToken;

        @Builder
        public TokensRes(String accessToken, String refreshToken) {
            this.accessToken = accessToken;
            this.refreshToken = refreshToken;
        }
    }
}
