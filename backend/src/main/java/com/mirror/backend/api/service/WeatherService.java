package com.mirror.backend.api.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.mirror.backend.api.dto.MidtermForecast;
import com.mirror.backend.api.dto.MidtermWeatherForecast;
import com.mirror.backend.api.dto.ShortTermForecast;
import com.mirror.backend.api.dto.UltraShortTermForecast;
import org.json.simple.JSONArray;

public interface WeatherService {
    JSONArray getWeatherInfo(StringBuilder urlBuilder) throws Exception;
    ShortTermForecast getShortTermForecast(JSONArray jsonArray);
    UltraShortTermForecast getUltraShortTermForecast(JSONArray jsonArray);
    MidtermForecast getMidtermForecast(JSONArray jsonArray) throws JsonProcessingException;
    MidtermWeatherForecast getMidtermWeatherForecast(JSONArray jsonArray) throws JsonProcessingException;
}
