package com.mirror.backend.api.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.ToString;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@AllArgsConstructor
@ToString
@RedisHash(value = "video", timeToLive = 30)
public class VideoMessage {

    @Id
    private Integer userId;
    private Integer sendUserId;
    private String videoPath;
    private String voicePath;
}
