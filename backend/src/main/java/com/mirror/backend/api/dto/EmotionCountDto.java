package com.mirror.backend.api.dto;

import com.mirror.backend.api.entity.EmotionCount;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;

import java.time.LocalDate;
import java.util.List;
import java.util.stream.Collectors;

public class EmotionCountDto {
    private LocalDate date;
    private List<EmotionOneDay> emotionList;


    public static class EmotionOneDay {
        private int emotionId;
        private int emotionCount;

        @Builder
        public EmotionOneDay(int emotionId, int emotionCount) {
            this.emotionId = emotionId;
            this.emotionCount = emotionCount;
        }
    }

    @Getter
    @AllArgsConstructor
    public static class EmotionCountRes {
        private int emotionCode;
        private int emotionCount;

        public EmotionCountRes(EmotionCount emotionCount) {
            this.emotionCode = emotionCount.getEmotionKey().getEmotionCode();
            this.emotionCount = emotionCount.getEmotionCount();
        }
    }
}
