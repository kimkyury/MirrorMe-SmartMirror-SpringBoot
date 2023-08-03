package com.mirror.backend.api.entity;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@Builder
@RedisHash("token")
public class RedisUserToken {

    @Id
    private String userEmail;
    private String accessToken;
    private String refreshToken;

    public RedisUserToken(String userEmail, String accessToken, String refreshToken) {
        this.userEmail = userEmail;
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
    }
}
