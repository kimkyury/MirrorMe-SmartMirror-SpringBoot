package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@RedisHash("isRainy")
public class RedisIsRainy {

    @Id
    private String householdId;
    private String isRainyCode;
    private String isRainyText;
    private String targetDay;

    @Builder
    public RedisIsRainy(String householdId, String isRainyCode, String isRainyText, String targetDay) {
        this.householdId = householdId;
        this.isRainyCode = isRainyCode;
        this.isRainyText = isRainyText;
        this.targetDay = targetDay;
    }
}
