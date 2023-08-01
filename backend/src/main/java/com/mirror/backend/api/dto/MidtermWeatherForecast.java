package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Getter;

@Getter
@JsonIgnoreProperties(ignoreUnknown = true)
public class MidtermWeatherForecast {
    private int rnSt3Am; // 3일 후 오전 강수 확률
    private int rnSt3Pm; // 3일 후 오후 강수 확률
    private int rnSt4Am; // 4일 후 오전 강수 확률
    private int rnSt4Pm; // 4일 후 오후 강수 확률
    private int rnSt5Am; // 5일 후 오전 강수 확률
    private int rnSt5Pm; // 5일 후 오후 강수 확률
    private int rnSt6Am; // 6일 후 오전 강수 확률
    private int rnSt6Pm; // 6일 후 오후 강수 확률
    private int rnSt7Am; // 7일 후 오전 강수 확률
    private int rnSt7Pm; // 7일 후 오후 강수 확률
}
