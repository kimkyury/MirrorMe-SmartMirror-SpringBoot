package com.mirror.backend.api.dto;


import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class RequestLoginDto {

    @JsonProperty("userEmail")
    String userEmail;
    @JsonProperty("password")
    String password;

    @Builder
    public RequestLoginDto(String userEmail, String password) {
        this.userEmail = userEmail;
        this.password = password;
    }

    @Override
    public String toString() {
        return "RequestLoginDto{" +
                "userEmail='" + userEmail + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}
