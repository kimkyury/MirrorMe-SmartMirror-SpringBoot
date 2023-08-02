package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class IotRequestUserDto {

    String mirrorId;

    @Override
    public String toString() {
        return "IotRequestUserDto{" +
                "mirrorId='" + mirrorId + '\'' +
                '}';
    }
}
