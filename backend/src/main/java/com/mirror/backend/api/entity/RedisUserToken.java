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
    private String userId;
    private String accessToken;
    private String refreshToken;

    public RedisUserToken(String userId, String accessToken, String refreshToken) {
        this.userId = userId;
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
    }


}
