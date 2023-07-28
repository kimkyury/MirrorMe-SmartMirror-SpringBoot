package com.mirror.backend.api.entity;


import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@RedisHash("accessToken")
public class RedisUserAccessToken {

    @Id
    private String userId;
    private String accessToken;

    public RedisUserAccessToken(String userId, String accessToken) {
        this.userId = userId;
        this.accessToken = accessToken;
    }
}
