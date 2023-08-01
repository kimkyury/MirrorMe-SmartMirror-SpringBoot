package com.mirror.backend.api.entity;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.ToString;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@ToString
@RedisHash(value = "video", timeToLive = 30)
public class VideoMessage {

    @Id
    private String userId;
    private String sendUserId;
    private String fileName;
    private String type;

    @Builder
    public VideoMessage(String userId, String sendUserId, String fileName, String type) {
        this.userId = userId;
        this.sendUserId = sendUserId;
        this.fileName = fileName;
        this.type = type;
    }
}
