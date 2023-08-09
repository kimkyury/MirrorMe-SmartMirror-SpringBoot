package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@JsonIgnoreProperties(ignoreUnknown = true)
public class ResponseTokensDto {

    @JsonProperty("accessToken")
    private String accessToken;
    @JsonProperty("refreshToken")
    private String refreshToken;
    @JsonProperty("isInitUser")
    private int isInitUser;

    @Builder
    public ResponseTokensDto(String accessToken, String refreshToken, int isInitUser) {
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
        this.isInitUser = isInitUser;
    }

    @Override
    public String toString() {
        return "ResponseTokensDto{" +
                "accessToken='" + accessToken + '\'' +
                ", refreshToken='" + refreshToken + '\'' +
                ", isInitUser='" + isInitUser + '\'' +
                '}';
    }
}
