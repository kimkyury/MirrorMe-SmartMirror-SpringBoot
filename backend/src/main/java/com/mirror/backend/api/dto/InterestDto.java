package com.mirror.backend.api.dto;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

public class InterestDto {

    @Getter
    @Setter
    @ToString
    public static class InterestReq{

        Long interestCode;
    }

    @Getter
    @ToString
    public static class InterestRes{

        private Long interestCode;
        private String interestName;

        @Builder
        public InterestRes(Long interestCode, String interestName) {
            this.interestCode = interestCode;
            this.interestName = interestName;
        }
    }
}
