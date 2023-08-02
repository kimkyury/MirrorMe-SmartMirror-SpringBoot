package com.mirror.backend.api.entity;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@NoArgsConstructor
@RedisHash(value = "video", timeToLive = 30)
public class VideoMessage {

    @Id
    private String userEmail;
    private String sendUserEmail;
    private String fileName;
    private String type;

    @Builder
    public VideoMessage(String userEmail, String sendUserEmail, String fileName, String type) {
        this.userEmail = userEmail;
        this.sendUserEmail = sendUserEmail;
        this.fileName = fileName;
        this.type = type;
    }
}
