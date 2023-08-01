package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class RequestConnectUserInfoDto {

    Long connectUserId;
    String connectUserAlias;

    @Override
    public String toString() {
        return "RequestConnectUserInfoDto{" +
                "connectUserId='" + connectUserId + '\'' +
                ", connectUserAlias='" + connectUserAlias + '\'' +
                '}';
    }
}
