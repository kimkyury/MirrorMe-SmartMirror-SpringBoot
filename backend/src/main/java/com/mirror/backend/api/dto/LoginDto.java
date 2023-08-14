package com.mirror.backend.api.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import javax.validation.constraints.NotNull;

public class LoginDto {

    @Getter
    @Setter
    @ToString
    public static class LoginReq{

        @NotNull
         private String userEmail;

        @NotNull
         private String password;
    }

    @Getter
    @ToString
    public static class LoginRes{

        private int isInitLoginUser;
        private String accessToken;
        private String  refreshToken;

        @Builder
        public LoginRes(int isInitLoginUser, String accessToken, String refreshToken) {
            this.isInitLoginUser = isInitLoginUser;
            this.accessToken = accessToken;
            this.refreshToken = refreshToken;
        }
    }
}
