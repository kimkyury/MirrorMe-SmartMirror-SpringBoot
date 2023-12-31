package com.mirror.backend.api.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import javax.validation.constraints.NotNull;

public class ConnectUserDto {

    @Getter
    @Setter
    @ToString
    public static class ConnectUserReq{

        @NotNull
        private Long connectUserId;
        @NotNull
        private String ConnectUserAlias;
    }

    @Getter
    @ToString
    public static class ConnectUserRes{

        private Long connectUserId;
        private String connectUserName;
        private String connectUserAlias;

        @Builder
        public ConnectUserRes(Long connectUserId, String connectUserName, String connectUserAlias) {
            this.connectUserId = connectUserId;
            this.connectUserName = connectUserName;
            this.connectUserAlias = connectUserAlias;
        }
    }
}
