package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.ShortTermForecast;
import com.mirror.backend.common.utils.ApiUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.time.LocalDate;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/weather")
public class WeatherController {

    private String dangiUrl = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst";

    @Value("${data.service-key}")
    private String serviceKey;

    @GetMapping
    public ApiUtils.ApiResult<ShortTermForecast> getDangiWeather() throws Exception {
        // user의 nx, ny 받아오는 로직 추가
        int nx = 55, ny = 127;
        String date = LocalDate.now().toString().replaceAll("-", "");

        StringBuilder urlBuilder = new StringBuilder(dangiUrl); /*URL*/
        urlBuilder.append("?" +  "serviceKey=" + serviceKey);
        urlBuilder.append("&" + URLEncoder.encode("pageNo","UTF-8") + "=" + URLEncoder.encode("1", "UTF-8")); /*페이지번호*/
        urlBuilder.append("&" + URLEncoder.encode("numOfRows","UTF-8") + "=" + URLEncoder.encode("266", "UTF-8")); /*한 페이지 결과 수*/
        urlBuilder.append("&" + URLEncoder.encode("dataType","UTF-8") + "=" + URLEncoder.encode("JSON", "UTF-8")); /*요청자료형식(XML/JSON) */
        urlBuilder.append("&" + URLEncoder.encode("base_date","UTF-8") + "=" + URLEncoder.encode(date, "UTF-8")); /*‘21년 6월 28일 발표*/
        urlBuilder.append("&" + URLEncoder.encode("base_time","UTF-8") + "=" + URLEncoder.encode("0200", "UTF-8")); /*06시 발표(정시단위) */
        urlBuilder.append("&" + URLEncoder.encode("nx","UTF-8") + "=" + URLEncoder.encode(String.valueOf(nx), "UTF-8")); /*예보지점의 X 좌표값*/
        urlBuilder.append("&" + URLEncoder.encode("ny","UTF-8") + "=" + URLEncoder.encode(String.valueOf(ny), "UTF-8")); /*예보지점의 Y 좌표값*/
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

        ShortTermForecast shortTermForecast = new ShortTermForecast();
        for(int i=0; i<parse_item.size(); i++) {
            JSONObject object = (JSONObject) parse_item.get(i);
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
        shortTermForecast.setDate(date);
        return success(shortTermForecast);
    }


}
