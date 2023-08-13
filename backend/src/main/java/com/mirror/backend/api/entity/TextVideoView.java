package com.mirror.backend.api.entity;


import lombok.Builder;
import lombok.Getter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@RedisHash("textVideoView")
public class TextVideoView {

    @Id
    private String userEmail;
    private String senderUserId;
    private String textVideoView;
    private String targetDay;

    @Builder
    public TextVideoView(String userEmail, String senderUserId, String textVideoView, String targetDay) {
        this.userEmail = userEmail;
        this.senderUserId = senderUserId;
        this.textVideoView = textVideoView;
        this.targetDay = targetDay;
    }
}
