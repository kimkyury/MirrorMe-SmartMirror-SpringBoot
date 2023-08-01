package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UltraShortTermForecast {
    private String date;
    private double T1H; // 기온
    private int RN1; // 1시간 강수량
    private double REH; // 습도
    private int PTY; // 강수형태
}
