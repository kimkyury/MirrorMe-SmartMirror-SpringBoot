package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@JsonIgnoreProperties(ignoreUnknown = true)
public class ResponseLoginDto {

    @JsonProperty("isInitLoginUser")
    private int isInitLoginUser;
    @JsonProperty("accessToken")
    private String accessToken;
    @JsonProperty("refreshToken")
    private String refreshToken;

    @Builder
    public ResponseLoginDto(int isInitLoginUser, String accessToken, String refreshToken) {
        this.isInitLoginUser = isInitLoginUser;
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
    }

    @Override
    public String toString() {
        return "ResponseLogin{" +
                "isInitLoginUser=" + isInitLoginUser +
                ", accessToken='" + accessToken + '\'' +
                ", refreshToken='" + refreshToken + '\'' +
                '}';
    }
}
