package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@RedisHash("summeryCalendar")
public class RedisSummeryCalendar {

    @Id
    private String userEmail;
    private String summeryCalendar;
    private String targetDay;

    @Builder
    public RedisSummeryCalendar(String userEmail, String summeryCalendar, String targetDay) {
        this.userEmail = userEmail;
        this.summeryCalendar = summeryCalendar;
        this.targetDay = targetDay;
    }
}
