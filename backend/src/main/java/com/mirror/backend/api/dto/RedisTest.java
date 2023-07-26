package com.mirror.backend.api.dto;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@RedisHash("videourl") // 최종적인키: videourl{id}
public class RedisTest {

    @Id
    private String userId;
    private String videoUrl;

    public RedisTest(String userId, String videoUrl){
        this.userId = userId;
        this.videoUrl = videoUrl;
    }
}
