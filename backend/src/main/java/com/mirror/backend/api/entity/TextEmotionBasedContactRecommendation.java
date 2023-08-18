package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@RedisHash("textEmotionBasedContactRecommendation")
public class TextEmotionBasedContactRecommendation {

    @Id
    private String userEmail;
    private String textEmotionBasedContactRecommendation;
    private String targetDay;

    @Builder
    public TextEmotionBasedContactRecommendation(String userEmail, String textEmotionBasedContactRecommendation, String targetDay) {
        this.userEmail = userEmail;
        this.textEmotionBasedContactRecommendation = textEmotionBasedContactRecommendation;
        this.targetDay = targetDay;
    }
}

