package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.dto.ShortTermForecast;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.api.service.impl.WeatherServiceImpl;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.json.simple.JSONArray;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.net.URLEncoder;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Iterator;
import java.util.List;

@Component
@RequiredArgsConstructor
public class WeatherRainyScheduler {

    @Value("${data.service-key}")
    private String dataServiceKey;

    public final RedisUserTokenRepository redisUserTokenRepository;
    public final RedisIsRainyRepository redisIsRainyRepository;
    public final HouseholdRepository householdRepository;
    public final WeatherServiceImpl weatherService;
    public final TokenUtil tokenUtil;

//    @Scheduled(cron = "40 * * * * ?")   // 개발용, 매분 30초마다 실행
    @Scheduled(cron = "0 0 0/3 * * ?") // 배포용, 매일 자정기준 3시간 마다 실행
    public void fetchRedisData() {

        System.out.println("------------Scheduler: Warning RainyWeather ----------");

        // 모든 household 가져오기
        Iterable<Household> householdsIterable = householdRepository.findAll();
        Iterator<Household> iterator = householdsIterable.iterator();

        while (iterator.hasNext()) {

            // household의 좌표값 얻기
            Household householdInfo = iterator.next();
            int ny = householdInfo.getGridNy();
            int nx = householdInfo.getGridNx();

            // 기상API를 통해 날씨가 어떤지 확인하기
            String HHMM = getCurrentTimeRange();
            String YYYYMMDD = EtcUtil.getTodayYYYYMMDD();
            if ( HHMM.equals("2300")){
                YYYYMMDD = String.valueOf(Integer.parseInt(YYYYMMDD) - 1);
            }

            boolean result = isRainyDay(nx, ny, YYYYMMDD,HHMM);
            saveRedisIsRainy(result, String.valueOf(householdInfo.getHouseholdId()));
        }

        System.out.println("------------ Finish Scheduler ----------");
    }

    public String getCurrentTimeRange(){

        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HHMM");
        String currentTime = now.format(formatter);

        if (currentTime.compareTo("1200") >= 0 && currentTime.compareTo("0211") < 0) return "2300";
        if (currentTime.compareTo("0211") >= 0 && currentTime.compareTo("0511") < 0) return "0200";
        if (currentTime.compareTo("0511") >= 0 && currentTime.compareTo("0811") < 0) return "0500";
        if (currentTime.compareTo("0811") >= 0 && currentTime.compareTo("1111") < 0) return "0800";
        if (currentTime.compareTo("1111") >= 0 && currentTime.compareTo("1411") < 0) return "1100";
        if (currentTime.compareTo("1411") >= 0 && currentTime.compareTo("1711") < 0) return "1400";
        if (currentTime.compareTo("1711") >= 0 && currentTime.compareTo("2011") < 0) return "1700";
        if (currentTime.compareTo("2011") >= 0 && currentTime.compareTo("2311") < 0) return "2000";

        return "2300";
    }

    private boolean isRainyDay(int nx, int ny, String baseDate, String baseTime) {

         String weatherUrl = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0";
         StringBuilder urlBuilder = null;

        try {
            urlBuilder = new StringBuilder(weatherUrl + "/getVilageFcst"); /*URL*/
            urlBuilder.append("?" + "serviceKey=" + dataServiceKey);
            urlBuilder.append("&" + URLEncoder.encode("pageNo", "UTF-8") + "=" + URLEncoder.encode("1", "UTF-8")); /*페이지번호*/
            urlBuilder.append("&" + URLEncoder.encode("numOfRows", "UTF-8") + "=" + URLEncoder.encode("14", "UTF-8")); /*한 페이지 결과 수*/
            urlBuilder.append("&" + URLEncoder.encode("dataType", "UTF-8") + "=" + URLEncoder.encode("JSON", "UTF-8")); /*요청자료형식(XML/JSON) */
            urlBuilder.append("&base_date=" + baseDate);
            urlBuilder.append("&base_time=" + baseTime);
            urlBuilder.append("&" + URLEncoder.encode("nx", "UTF-8") + "=" + URLEncoder.encode(String.valueOf(nx), "UTF-8")); /*예보지점의 X 좌표값*/
            urlBuilder.append("&" + URLEncoder.encode("ny", "UTF-8") + "=" + URLEncoder.encode(String.valueOf(ny), "UTF-8")); /*예보지점의 Y 좌표값*/
        } catch(Exception e){
            e.getStackTrace();
        }

        List<ShortTermForecast> shortTermForecast = null;
        try {
            JSONArray weatherInfo = weatherService.getWeatherInfo(urlBuilder);
            shortTermForecast = weatherService.getShortTermForecast(weatherInfo, baseDate);
        }catch(Exception e){
            e.getStackTrace();
        }

        for(ShortTermForecast shortTermForecast1 : shortTermForecast){
            if (shortTermForecast1.getPTY() == 1 || shortTermForecast1.getPTY() == 2)
                return false;
        }
        return true;
    }

    public void saveRedisIsRainy(boolean isRainy, String householdId){

        TextCautionRainy textCautionRainy = null;

        if (isRainy){
            textCautionRainy = TextCautionRainy.builder()
                    .householdId(householdId)
                    .isRainyCode("1")
                    .isRainyText("오늘은 비가 올텐데, 나가신다면 우산 가져가세요!")
                    .build();
        }else{
            textCautionRainy = TextCautionRainy.builder()
                    .householdId(String.valueOf(householdId))
                    .isRainyCode("0")
                    .isRainyText("오늘은 비가 안 와요!")
                    .build();
        }

        redisIsRainyRepository.save(textCautionRainy);
    }


}
