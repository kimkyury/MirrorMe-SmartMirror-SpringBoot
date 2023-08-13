package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

public class ConnectUserDto {

    @Getter
    @Setter
    @ToString
    public static class ConnectUserReq{
        private Long connectUserId;
        private String ConnectUserAlias;
    }


}
