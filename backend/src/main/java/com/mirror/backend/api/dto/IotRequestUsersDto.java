package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class IotRequestUsersDto {

    String mirrorId;


    @Override
    public String toString() {
        return "IotRequestUserDto{" +
                "mirrorId='" + mirrorId + '\'' +
                '}';
    }
}
