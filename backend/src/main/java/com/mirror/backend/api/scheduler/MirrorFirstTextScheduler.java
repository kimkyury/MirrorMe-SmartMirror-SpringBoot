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
import java.util.Optional;

@Component
public class MirrorFirstTextScheduler {

    public final RedisUserTokenRepository redisUserTokenRepository;
    public final RedisSummeryCalendarRepository redisSummeryCalendarRepository;
    public final CalendarService calendarService;
    public final ChatGptUtil chatGptUtil;
    public final OAuthService oAuthService;
    public final TokenUtil tokenUtil;

    @Autowired
    public MirrorFirstTextScheduler(RedisUserTokenRepository redisUserTokenRepository,
                                    RedisSummeryCalendarRepository redisSummeryCalendarRepository,
                                    CalendarService calendarService, ChatGptUtil chatGptUtil, OAuthService oAuthService, TokenUtil tokenUtil) {
        this.redisUserTokenRepository = redisUserTokenRepository;
        this.redisSummeryCalendarRepository = redisSummeryCalendarRepository;
        this.calendarService = calendarService;
        this.chatGptUtil = chatGptUtil;
        this.oAuthService = oAuthService;
        this.tokenUtil = tokenUtil;
    }

//    @Scheduled(cron = "20 * * * * ?")   // 개발용, 매분 20초마다 실행
//    @Scheduled(cron = "20 0 0 * * ?") // 배용, 매일 자정 20초마다 실행
    public void fetchRedisData() {

        // 오늘 날씨가 비오는 날인지 확인한다

        // 해당 유저의 3줄 요약 정보가 있는지 확인한다


        // 해당 유저의 친인척의 생일 정보가 있는지 확인한다

        // 해당 유저의 친인척의 생일을 추천해줄만한 게 있는지 확인한다


    }

    public String getSummeryCalendar(String userEmail){

        Optional<RedisSummeryCalendar> redisSummeryCalendarOptional = redisSummeryCalendarRepository.findById(userEmail);

//        if (redisSummeryCalendarOptional.is)
        return null;

    }



}
