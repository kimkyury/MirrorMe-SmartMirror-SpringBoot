package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.MidtermForecast;
import com.mirror.backend.api.dto.MidtermWeatherForecast;
import com.mirror.backend.api.dto.ShortTermForecast;
import com.mirror.backend.api.dto.UltraShortTermForecast;
import com.mirror.backend.api.service.WeatherService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import org.json.simple.JSONArray;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.net.URLEncoder;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/weather")
public class WeatherController {

    private String weatherUrl = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0";
    private String midWeatherUrl = "http://apis.data.go.kr/1360000/MidFcstInfoService";

    @Value("${data.service-key}")
    private String serviceKey;

    @Autowired
    private WeatherService weatherService;

    @GetMapping("/short")
    @Operation(summary = "단기 예보 조회", description = "새벽 2시로 해야 최저, 최고 기온 뜬다. 이 후 시간은 0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300 (1일 8회) 업데이트된다.")
    public ApiUtils.ApiResult<List<ShortTermForecast>> shortTermForecastApi(@RequestParam String pageNo, @RequestParam String numOfRows, @RequestParam String baseDate, @RequestParam String baseTime) throws Exception {
        // user의 nx, ny 받아오는 로직 추가
        int nx = 55, ny = 127;

        StringBuilder urlBuilder = new StringBuilder(weatherUrl + "/getVilageFcst"); /*URL*/
        urlBuilder.append("?" +  "serviceKey=" + serviceKey);
        urlBuilder.append("&" + URLEncoder.encode("pageNo","UTF-8") + "=" + URLEncoder.encode(pageNo, "UTF-8")); /*페이지번호*/
        urlBuilder.append("&" + URLEncoder.encode("numOfRows","UTF-8") + "=" + URLEncoder.encode(numOfRows, "UTF-8")); /*한 페이지 결과 수*/
        urlBuilder.append("&" + URLEncoder.encode("dataType","UTF-8") + "=" + URLEncoder.encode("JSON", "UTF-8")); /*요청자료형식(XML/JSON) */
        urlBuilder.append("&base_date=" + baseDate);
        urlBuilder.append("&base_time=" + baseTime);
        urlBuilder.append("&" + URLEncoder.encode("nx","UTF-8") + "=" + URLEncoder.encode(String.valueOf(nx), "UTF-8")); /*예보지점의 X 좌표값*/
        urlBuilder.append("&" + URLEncoder.encode("ny","UTF-8") + "=" + URLEncoder.encode(String.valueOf(ny), "UTF-8")); /*예보지점의 Y 좌표값*/

        JSONArray weatherInfo = weatherService.getWeatherInfo(urlBuilder);
        return success(weatherService.getShortTermForecast(weatherInfo, baseDate));
    }

    @GetMapping("/ultra")
    @Operation(summary = "초단기 실황 조회", description = "매시간 30분마다 업데이트 된다.")
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

    @GetMapping("/mid")
    @Operation(summary = "중기 최저, 최고 기온 조회", description = "매일 오전 6시에 정보 뜬다. 6시에 조회하는 요청 들어가기")
    public ApiUtils.ApiResult<MidtermForecast> midtermForecastApi(@RequestParam String pageNo, @RequestParam String numOfRows) throws Exception{
        // user의 예보구역코드 받아오는 로직 추가
        String regId = "11H20201";

        String date = LocalDate.now().toString().replaceAll("-", "") + "0600";
        StringBuilder urlBuilder = new StringBuilder(midWeatherUrl + "/getMidTa"); /*URL*/
        urlBuilder.append("?" +  "serviceKey=" + serviceKey);
        urlBuilder.append("&" + URLEncoder.encode("pageNo","UTF-8") + "=" + URLEncoder.encode(pageNo, "UTF-8"));
        urlBuilder.append("&" + URLEncoder.encode("numOfRows","UTF-8") + "=" + URLEncoder.encode(numOfRows, "UTF-8"));
        urlBuilder.append("&" + URLEncoder.encode("dataType","UTF-8") + "=" + URLEncoder.encode("JSON", "UTF-8"));
        urlBuilder.append("&" + URLEncoder.encode("regId","UTF-8") + "=" + URLEncoder.encode(regId, "UTF-8")); // 예보구역코드
        urlBuilder.append("&tmFc=" + date);

        JSONArray weatherInfo = weatherService.getWeatherInfo(urlBuilder);
        MidtermForecast midtermForecast = weatherService.getMidtermForecast(weatherInfo);

        return success(midtermForecast);
    }

    @GetMapping("/mid/rain")
    @Operation(summary = "중기 비 예보", description = "매일 18시에 정보 뜬다. 18시에 조회하는 요청 들어가기")
    public ApiUtils.ApiResult<MidtermWeatherForecast> midtermRainForecastApi(@RequestParam String pageNo, @RequestParam String numOfRows) throws Exception{
        // user의 예보구역코드 받아오는 로직 추가
        String regId = "11H20201";

        String date = LocalDate.now().toString().replaceAll("-", "");
        String time = LocalTime.now().toString().substring(0, 2);
        if(Integer.parseInt(time) < 18) {
            date = LocalDate.now().minusDays(1).toString().replaceAll("-", "");
        }

        date += "1800";

        StringBuilder urlBuilder = new StringBuilder(midWeatherUrl + "/getMidLandFcst"); /*URL*/
        urlBuilder.append("?" +  "serviceKey=" + serviceKey);
        urlBuilder.append("&" + URLEncoder.encode("pageNo","UTF-8") + "=" + URLEncoder.encode(pageNo, "UTF-8"));
        urlBuilder.append("&" + URLEncoder.encode("numOfRows","UTF-8") + "=" + URLEncoder.encode(numOfRows, "UTF-8"));
        urlBuilder.append("&" + URLEncoder.encode("dataType","UTF-8") + "=" + URLEncoder.encode("JSON", "UTF-8"));
        urlBuilder.append("&" + URLEncoder.encode("regId","UTF-8") + "=" + URLEncoder.encode(regId, "UTF-8")); // 예보구역코드
        urlBuilder.append("&tmFc=" + date);

        JSONArray weatherInfo = weatherService.getWeatherInfo(urlBuilder);
        MidtermWeatherForecast midtermWeatherForecast = weatherService.getMidtermWeatherForecast(weatherInfo);
        return success(midtermWeatherForecast);
    }
}
