package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@RedisHash("mirrorFirstText")
public class RedisMirrorFirstText {

    @Id
    private String userEmail;
    private String textCode;
    private String textContent;
    private String isUsed;  // 테스트 환경을 위한 isUsed

    @Builder
    public RedisMirrorFirstText(String userEmail, String textCode, String textContent, String isUsed) {
        this.userEmail = userEmail;
        this.textCode = textCode;
        this.textContent = textContent;
        this.isUsed = isUsed;
    }
}
