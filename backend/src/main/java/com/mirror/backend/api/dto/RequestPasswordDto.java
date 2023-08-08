package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class RequestPasswordDto {

    @JsonProperty("userEmail")
    String userEmail;

    @JsonProperty("password")
    String password;

    @Override
    public String toString() {
        return "RequestPasswordDto{" +
                "password='" + password + '\'' +
                '}';
    }
}
