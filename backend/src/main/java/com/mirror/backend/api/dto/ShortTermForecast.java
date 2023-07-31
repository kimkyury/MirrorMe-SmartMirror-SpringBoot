package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
public class ShortTermForecast {
    private String date;
    private int POP; // 강수 확률
    private int PTY; // 강수 형태
    private double REH; // 습도
    private int SKY; // 하늘상태
    private double TMP; // 1시간 기온
    private double TMN; // 일 최저 기온
    private double TMX; // 일 최고 기온
}
