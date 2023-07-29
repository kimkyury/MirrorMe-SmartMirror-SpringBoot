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
    private Integer userId;
    private Integer sendUserId;
    private String videoPath;
    private String voicePath;

    @Builder
    public VideoMessage(Integer userId, Integer sendUserId, String videoPath, String voicePath) {
        this.userId = userId;
        this.sendUserId = sendUserId;
        this.videoPath = videoPath;
        this.voicePath = voicePath;
    }
}
