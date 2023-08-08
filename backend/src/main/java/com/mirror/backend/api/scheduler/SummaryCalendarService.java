package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.entity.RedisSummeryCalendar;
import com.mirror.backend.api.entity.RedisUserToken;
import com.mirror.backend.api.repository.RedisSummeryCalendarRepository;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.common.utils.ChatGptUtil;
import com.mirror.backend.common.utils.TokenUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Iterator;

@Component
public class SummaryCalendarService {

    public final RedisUserTokenRepository redisUserTokenRepository;
    public final RedisSummeryCalendarRepository redisSummeryCalendarRepository;
    public final CalendarService calendarService;
    public final ChatGptUtil chatGptUtil;
    public final OAuthService oAuthService;
    public final TokenUtil tokenUtil;

    @Autowired
    public SummaryCalendarService(RedisUserTokenRepository redisUserTokenRepository,
                                  RedisSummeryCalendarRepository redisSummeryCalendarRepository,
                                  CalendarService calendarService, ChatGptUtil chatGptUtil, OAuthService oAuthService, TokenUtil tokenUtil) {
        this.redisUserTokenRepository = redisUserTokenRepository;
        this.redisSummeryCalendarRepository = redisSummeryCalendarRepository;
        this.calendarService = calendarService;
        this.chatGptUtil = chatGptUtil;
        this.oAuthService = oAuthService;
        this.tokenUtil = tokenUtil;
    }

    // 1. Redis내의 유저 Token들을 모두 가져온다
//    @Scheduled(cron = "5 * * * * ?")   // 개발용, 매분 5초마다 실행
    @Scheduled(cron = "0 0 0 * * ?") // 배용, 매일 자정마다 실행
    public void fetchRedisData() {
        System.out.println("------------실행중----------");
        // redis내의 유저 Token을 가져온다
        Iterable<RedisUserToken> redisUserTokenIterable= redisUserTokenRepository.findAll();
        Iterator<RedisUserToken> iterator = redisUserTokenIterable.iterator();


        while (iterator.hasNext()) {
            RedisUserToken userTokenInfo = iterator.next();
            String accessToken = userTokenInfo.getAccessToken();
            String refreshToken = userTokenInfo.getRefreshToken();

           accessToken = tokenUtil.confirmAccessToken(accessToken, refreshToken);

            // 해당 유저의 Email을 조회
            String userEmail = oAuthService.getUserEmailFromAccessToken(accessToken);

            // 2. 해당 UserToken으로 Calendar내역을 각각 가져온다
            Event event = calendarService.getMyCalendar(accessToken, "primary");
            String eventInTodayList = getUserEventInToday(event);

            // 3. Gpt에게 해당 일정을 요약해달라는 요청을 보낸다
            String answer = getSummeryCalendarFromGPT(eventInTodayList);

            System.out.println(answer);

            saveRedisSummeryCalendar(answer, userEmail);

        }
    }

    public String getUserEventInToday(Event event){
        String userEventList;

        StringBuilder sb = new StringBuilder();
        LocalDate now = LocalDate.now();

        for( Event.Item item: event.getItems()) {
            String startTime = item.getStart().getDateTime();
            String endTime = item.getEnd().getDateTime();

            startTime = startTime == null ? item.getStart().getDate() : startTime.substring(0, 10);
            endTime = endTime == null ? item.getEnd().getDate() : endTime.substring(0, 10);
            DateTimeFormatter parser = DateTimeFormatter.ofPattern("yyyy-MM-dd");
            LocalDate localStartDate = LocalDate.parse(startTime, parser);
            LocalDate localEndDate = LocalDate.parse(endTime, parser);

            boolean chk = !now.isBefore(localStartDate) && !now.isAfter(localEndDate);
            if (chk) sb.append(item.getSummary() +", ");
        }
        userEventList = sb.toString();
        return userEventList;

    }

    // 3. 해당 Calendar내역을 3줄 요약하도록 GPT한테 요청한다
    public String  getSummeryCalendarFromGPT(String eventInTodayList){

        StringBuilder sb = new StringBuilder();
        sb.append("다음과 같은 일정이 있을 때, 가장 중요한 것 3가지를 뽑아 각 15자 이내로 1. 2. 3. 형식에 맞춰 요약해주세요.  ");
        sb.append(" // " + eventInTodayList + " // ");

        String answer = chatGptUtil.createMessage(sb.toString());

        return answer;

    }

    public void saveRedisSummeryCalendar(String summeryText, String userEmail){

        RedisSummeryCalendar summeryCalendar = RedisSummeryCalendar.builder()
                .userEmail(userEmail)
                .summeryCalendar(summeryText)
                .build();

        redisSummeryCalendarRepository.save(summeryCalendar);
    }



}
