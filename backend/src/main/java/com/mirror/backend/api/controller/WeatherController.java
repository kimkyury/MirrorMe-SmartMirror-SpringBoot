package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.ShortTermForecast;
import com.mirror.backend.api.dto.UltraShortTermForecast;
import com.mirror.backend.api.service.WeatherService;
import com.mirror.backend.common.utils.ApiUtils;
import org.json.simple.JSONArray;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.net.URLEncoder;
import java.time.LocalDate;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/weather")
public class WeatherController {

    private String weatherUrl = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0";

    @Value("${data.service-key}")
    private String serviceKey;

    @Autowired
    private WeatherService weatherService;

    @GetMapping("/short")
    public ApiUtils.ApiResult<ShortTermForecast> shortTermForecastApi(@RequestParam String pageNo, @RequestParam String numOfRows, @RequestParam String baseTime) throws Exception {
        // user의 nx, ny 받아오는 로직 추가
        int nx = 55, ny = 127;

        String date = LocalDate.now().toString().replaceAll("-", "");
        StringBuilder urlBuilder = new StringBuilder(weatherUrl + "/getVilageFcst"); /*URL*/
        urlBuilder.append("?" +  "serviceKey=" + serviceKey);
        urlBuilder.append("&" + URLEncoder.encode("pageNo","UTF-8") + "=" + URLEncoder.encode(pageNo, "UTF-8")); /*페이지번호*/
        urlBuilder.append("&" + URLEncoder.encode("numOfRows","UTF-8") + "=" + URLEncoder.encode(numOfRows, "UTF-8")); /*한 페이지 결과 수*/
        urlBuilder.append("&" + URLEncoder.encode("dataType","UTF-8") + "=" + URLEncoder.encode("JSON", "UTF-8")); /*요청자료형식(XML/JSON) */
        urlBuilder.append("&" + URLEncoder.encode("base_date","UTF-8") + "=" + URLEncoder.encode(date, "UTF-8"));
        urlBuilder.append("&base_time=" + baseTime);
        urlBuilder.append("&" + URLEncoder.encode("nx","UTF-8") + "=" + URLEncoder.encode(String.valueOf(nx), "UTF-8")); /*예보지점의 X 좌표값*/
        urlBuilder.append("&" + URLEncoder.encode("ny","UTF-8") + "=" + URLEncoder.encode(String.valueOf(ny), "UTF-8")); /*예보지점의 Y 좌표값*/

        JSONArray weatherInfo = weatherService.getWeatherInfo(urlBuilder);
        ShortTermForecast shortTermForecast = weatherService.getShortTermForecast(weatherInfo);

        shortTermForecast.setDate(date);
        return success(shortTermForecast);
    }

    @GetMapping("/ultra")
    public ApiUtils.ApiResult<UltraShortTermForecast> ultraShortTermForecastApi(@RequestParam String pageNo, @RequestParam String numOfRows, @RequestParam String baseTime) throws Exception {
        // user의 nx, ny 받아오는 로직 추가
        int nx = 55, ny = 127;

        String date = LocalDate.now().toString().replaceAll("-", "");
        StringBuilder urlBuilder = new StringBuilder(weatherUrl + "/getUltraSrtNcst"); /*URL*/
        urlBuilder.append("?" +  "serviceKey=" + serviceKey);
        urlBuilder.append("&" + URLEncoder.encode("pageNo","UTF-8") + "=" + URLEncoder.encode(pageNo, "UTF-8"));
        urlBuilder.append("&" + URLEncoder.encode("numOfRows","UTF-8") + "=" + URLEncoder.encode(numOfRows, "UTF-8"));
        urlBuilder.append("&" + URLEncoder.encode("dataType","UTF-8") + "=" + URLEncoder.encode("JSON", "UTF-8"));
        urlBuilder.append("&" + URLEncoder.encode("base_date","UTF-8") + "=" + URLEncoder.encode(date, "UTF-8"));
        urlBuilder.append("&base_time=" + baseTime);
        urlBuilder.append("&" + URLEncoder.encode("nx","UTF-8") + "=" + URLEncoder.encode(String.valueOf(nx), "UTF-8")); /*예보지점의 X 좌표값*/
        urlBuilder.append("&" + URLEncoder.encode("ny","UTF-8") + "=" + URLEncoder.encode(String.valueOf(ny), "UTF-8")); /*예보지점의 Y 좌표값*/

        JSONArray weatherInfo = weatherService.getWeatherInfo(urlBuilder);
        UltraShortTermForecast ultraShortTermForecast = weatherService.getUltraShortTermForecast(weatherInfo);

        ultraShortTermForecast.setDate(date);
        return success(ultraShortTermForecast);
    }
}
