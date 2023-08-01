package com.mirror.backend.api.service.impl;
import com.mirror.backend.api.dto.ShortTermForecast;
import com.mirror.backend.api.dto.UltraShortTermForecast;
import com.mirror.backend.api.service.WeatherService;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

@Service
public class WeatherServiceImpl implements WeatherService {
    @Override
    public JSONArray getWeatherInfo(StringBuilder urlBuilder) throws Exception {
        System.out.println("urlBuilder = " + urlBuilder);
        URL url = new URL(urlBuilder.toString());

        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Content-type", "application/json");
        System.out.println("Response code: " + conn.getResponseCode());

        BufferedReader rd;
        if (conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
            rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        } else {
            rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
        }
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = rd.readLine()) != null) {
            sb.append(line);
        }
        rd.close();
        conn.disconnect();
        String result = sb.toString();

        System.out.println(result);

        JSONParser jsonParser = new JSONParser();
        JSONObject jsonObject = (JSONObject) jsonParser.parse(result);
        JSONObject parse_response = (JSONObject) jsonObject.get("response");
        JSONObject parse_body = (JSONObject) parse_response.get("body");
        JSONObject parse_items = (JSONObject) parse_body.get("items");
        JSONArray parse_item = (JSONArray) parse_items.get("item");

        return parse_item;
    }

    @Override
    public ShortTermForecast getShortTermForecast(JSONArray weatherInfo) {
        ShortTermForecast shortTermForecast = new ShortTermForecast();
        for(int i=0; i<weatherInfo.size(); i++) {
            JSONObject object = (JSONObject) weatherInfo.get(i);
            String category = (String) object.get("category");
            String fcstValue = (String) object.get("fcstValue");
            switch (category) {
                case "POP":
                    shortTermForecast.setPOP(Integer.parseInt(fcstValue));
                    break;
                case "PTY":
                    shortTermForecast.setPTY(Integer.parseInt(fcstValue));
                    break;
                case "REH":
                    shortTermForecast.setREH(Integer.parseInt(fcstValue));
                    break;
                case "SKY":
                    shortTermForecast.setSKY(Integer.parseInt(fcstValue));
                    break;
                case "TMP":
                    shortTermForecast.setTMP(Integer.parseInt(fcstValue));
                    break;
                case "TMN":
                    shortTermForecast.setTMN(Double.parseDouble(fcstValue));
                    break;
                case "TMX":
                    shortTermForecast.setTMX(Double.parseDouble(fcstValue));
                    break;
            }
        }
        return shortTermForecast;
    }

    @Override
    public UltraShortTermForecast getUltraShortTermForecast(JSONArray weatherInfo) {
        UltraShortTermForecast ultraShortTermForecast = new UltraShortTermForecast();

        for(int i=0; i<weatherInfo.size(); i++) {
            JSONObject object = (JSONObject) weatherInfo.get(i);
            String category = (String) object.get("category");
            String fcstValue = (String) object.get("obsrValue");
            switch (category) {
                case "T1H":
                    ultraShortTermForecast.setT1H(Double.parseDouble(fcstValue));
                    break;
                case "PTY":
                    ultraShortTermForecast.setPTY(Integer.parseInt(fcstValue));
                    break;
                case "REH":
                    ultraShortTermForecast.setREH(Integer.parseInt(fcstValue));
                    break;
                case "RN1":
                    ultraShortTermForecast.setRN1(Integer.parseInt(fcstValue));
                    break;
            }
        }
        return ultraShortTermForecast;
    }
}
