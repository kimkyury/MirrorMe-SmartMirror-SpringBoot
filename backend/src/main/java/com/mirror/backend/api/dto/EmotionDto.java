package com.mirror.backend.api.dto;

import com.mirror.backend.api.entity.EmotionCount;
import lombok.Builder;
import lombok.Getter;

import java.time.LocalDate;
import java.util.List;

public class EmotionDto {

    @Getter
    public static class EmotionReq {
        private String emotionDate;
        private Long userId;
        private List<Integer> emotionList;
        private int emotionCode;
    }

    @Getter
    public static class EmotionRes {
        private String emotionDate;
        private List<EmotionCountDto.EmotionCountRes> emotionList;

        @Builder
        public EmotionRes(String emotionDate, List<EmotionCountDto.EmotionCountRes> emotionList) {
            this.emotionDate = emotionDate;
            this.emotionList = emotionList;
        }
    }

    @Getter
    public static class EmotionFamilyResList {
        private String connectUserAlias;
        private List<EmotionRes> emotionList;

        @Builder
        public EmotionFamilyResList(String connectUserAlias, List<EmotionRes> emotionList) {
            this.connectUserAlias = connectUserAlias;
            this.emotionList = emotionList;
        }
    }
}
