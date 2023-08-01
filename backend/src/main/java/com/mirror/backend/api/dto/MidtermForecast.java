package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Getter;

@Getter
@JsonIgnoreProperties(ignoreUnknown = true)
public class MidtermForecast {
    private int taMin3; // 3일 후 예상최저기온
    private int taMin3Low; // 3일 후 예상최저기온 하한 범위
    private int taMin3High; // 3일 후 예상최저기온 상한 범위
    private int taMax3; // 3일 후 예상최고기온
    private int taMax3Low; // 3일 후 예상최고기온 하한 범위
    private int taMax3High; // 3일 후 예상최고기온 상한 범위

    private int taMin4; // 4일 후 예상최저기온
    private int taMin4Low; // 4일 후 예상최저기온 하한 범위
    private int taMin4High; // 4일 후 예상최저기온 상한 범위
    private int taMax4; // 4일 후 예상최고기온
    private int taMax4Low; // 4일 후 예상최고기온 하한 범위
    private int taMax4High; // 4일 후 예상최고기온 상한 범위

    private int taMin5; // 5일 후 예상최저기온
    private int taMin5Low; // 5일 후 예상최저기온 하한 범위
    private int taMin5High; // 5일 후 예상최저기온 상한 범위
    private int taMax5; // 5일 후 예상최고기온
    private int taMax5Low; // 5일 후 예상최고기온 하한 범위
    private int taMax5High; // 5일 후 예상최고기온 상한 범위

    private int taMin6; // 6일 후 예상최저기온
    private int taMin6Low; // 6일 후 예상최저기온 하한 범위
    private int taMin6High; // 6일 후 예상최저기온 상한 범위
    private int taMax6; // 6일 후 예상최고기온
    private int taMax6Low; // 6일 후 예상최고기온 하한 범위
    private int taMax6High; // 6일 후 예상최고기온 상한 범위

    private int taMin7; // 7일 후 예상최저기온
    private int taMin7Low; // 7일 후 예상최저기온 하한 범위
    private int taMin7High; // 7일 후 예상최저기온 상한 범위
    private int taMax7; // 7일 후 예상최고기온
    private int taMax7Low; // 7일 후 예상최고기온 하한 범위
    private int taMax7High; // 7일 후 예상최고기온 상한 범위
}
