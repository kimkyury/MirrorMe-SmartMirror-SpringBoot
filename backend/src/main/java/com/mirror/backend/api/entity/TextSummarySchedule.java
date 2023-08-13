package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@RedisHash("textSummarySchedule")
public class TextSummarySchedule {

    @Id
    private String userEmail;
    private String textSummarySchedule;
    private String targetDay;

    @Builder
    public TextSummarySchedule(String userEmail, String textSummarySchedule, String targetDay) {
        this.userEmail = userEmail;
        this.textSummarySchedule = textSummarySchedule;
        this.targetDay = targetDay;
    }
}
