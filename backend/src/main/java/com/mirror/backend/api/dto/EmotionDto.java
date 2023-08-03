package com.mirror.backend.api.dto;

import lombok.Getter;

import java.util.List;

public class EmotionDto {

    @Getter
    public static class EmotionReq {
        private String emotionDate;
        private Long userId;
        private List<Integer> emotionList;
        private int emotionCode;
    }

}
