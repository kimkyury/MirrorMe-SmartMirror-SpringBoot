package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.ShortTermForecast;
import com.mirror.backend.api.dto.UltraShortTermForecast;
import org.json.simple.JSONArray;

public interface WeatherService {
    JSONArray getWeatherInfo(StringBuilder urlBuilder) throws Exception;
    ShortTermForecast getShortTermForecast(JSONArray jsonArray);
    UltraShortTermForecast getUltraShortTermForecast(JSONArray jsonArray);
}
