package com.mirror.backend.api.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.mirror.backend.api.dto.*;
import org.json.simple.JSONArray;

import java.util.List;

public interface WeatherService {
    JSONArray getWeatherInfo(StringBuilder urlBuilder) throws Exception;
    List<ShortTermForecast> getShortTermForecast(JSONArray jsonArray, String date);
    UltraShortTermForecast getUltraShortTermForecast(JSONArray jsonArray);
    MidtermForecast getMidtermForecast(JSONArray jsonArray) throws JsonProcessingException;
    MidtermWeatherForecast getMidtermWeatherForecast(JSONArray jsonArray) throws JsonProcessingException;

    HouseholdDto.HouseHoldLocationRes getUserLocation(Long householdId);
}
