package com.mirror.backend.api.entity;


import lombok.Getter;
import org.springframework.data.redis.core.RedisHash;

@Getter
@RedisHash("textSummarySchedule")
public class TextVideoView {
}
