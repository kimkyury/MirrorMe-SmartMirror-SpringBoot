package com.mirror.backend.api.dto;

import lombok.Getter;

public class EmotionDto {

    @Getter
    public static class EmotionReq {
        private String emotionDate;
        private Long userId;
        private int emotionCode;
    }
}
