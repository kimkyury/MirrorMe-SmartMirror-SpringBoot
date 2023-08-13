package com.mirror.backend.api.entity;


import lombok.Builder;
import lombok.Getter;
import lombok.ToString;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@RedisHash("googleOauthToken")
@ToString
public class GoogleOAuthToken {

    @Id
    private String userEmail;
    private String accessToken;
    private String refreshToken;

    @Builder
    public GoogleOAuthToken(String userEmail, String accessToken, String refreshToken) {
        this.userEmail = userEmail;
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
    }
}
