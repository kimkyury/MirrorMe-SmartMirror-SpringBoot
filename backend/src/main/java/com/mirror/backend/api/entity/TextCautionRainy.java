package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@RedisHash("textCautionRainy")
public class TextCautionRainy {

    @Id
    private String householdId;
    private String isRainyCode;
    private String textCautionRainy;
    private String targetDay;

    @Builder
    public TextCautionRainy(String householdId, String isRainyCode, String textCautionRainy, String targetDay) {
        this.householdId = householdId;
        this.isRainyCode = isRainyCode;
        this.textCautionRainy = textCautionRainy;
        this.targetDay = targetDay;
    }
}
