package com.mirror.backend.api.dto;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

public class MirrorDto {

    @Getter
    @Setter
    @ToString
    public static class MirrorReq{

        private String mirrorId;
        private Long mirrorPlaceCode;
    }

    @Getter
    @ToString
    public static class MirrorRes{

        private String mirrorId;
        private Long mirrorPlaceCode;

        @Builder
        public MirrorRes(String mirrorId, Long mirrorPlaceCode){
            this.mirrorId = mirrorId;
            this.mirrorPlaceCode = mirrorPlaceCode;
        }
    }
}
