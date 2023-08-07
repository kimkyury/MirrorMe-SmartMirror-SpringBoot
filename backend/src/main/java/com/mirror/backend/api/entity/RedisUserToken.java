package com.mirror.backend.api.entity;


import lombok.Builder;
import lombok.Getter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@RedisHash("token")
public class RedisUserToken {

    @Id
    private String userEmail;
    private String accessToken;
    private String refreshToken;

    @Builder
    public RedisUserToken(String userEmail, String accessToken, String refreshToken) {
        this.userEmail = userEmail;
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
    }

    @Override
    public String toString() {
        return "RedisUserToken{" +
                "userEmail='" + userEmail + '\'' +
                ", accessToken='" + accessToken + '\'' +
                ", refreshToken='" + refreshToken + '\'' +
                '}';
    }
}
