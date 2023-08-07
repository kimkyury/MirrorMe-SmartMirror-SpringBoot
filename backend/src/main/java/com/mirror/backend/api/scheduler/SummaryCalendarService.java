package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.entity.RedisSummeryCalendar;
import com.mirror.backend.api.entity.RedisUserToken;
import com.mirror.backend.api.info.ChatGPT;
import com.mirror.backend.api.repository.RedisSummeryCalendarRepository;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import com.mirror.backend.api.service.CalendarService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Iterator;
import java.util.List;

@Component
public class SummaryCalendarService {

    public final RedisUserTokenRepository redisUserTokenRepository;
    public final RedisSummeryCalendarRepository redisSummeryCalendarRepository;
    public final CalendarService calendarService;
    public final ChatGPT chatGPT;

    @Autowired
    public SummaryCalendarService(RedisUserTokenRepository redisUserTokenRepository,
                                  RedisSummeryCalendarRepository redisSummeryCalendarRepository,
                                  CalendarService calendarService, ChatGPT chatGPT) {
        this.redisUserTokenRepository = redisUserTokenRepository;
        this.redisSummeryCalendarRepository = redisSummeryCalendarRepository;
        this.calendarService = calendarService;
        this.chatGPT = chatGPT;
    }

    // 1. Redis내의 유저 Token들을 모두 가져온다
    @Scheduled(cron = "5 * * * * ?")
    public void fetchRedisData() {
        System.out.println("------------실행중----------");
        // redis내의 유저 Token을 가져온다
        Iterable<RedisUserToken> redisUserTokenIterable= redisUserTokenRepository.findAll();
        Iterator<RedisUserToken> iterator = redisUserTokenIterable.iterator();

        while (iterator.hasNext()) {
            RedisUserToken userTokenInfo = iterator.next();
            String accessToken = userTokenInfo.getAccessToken();

            // 만료될시 재발급하는 로직 추가해야함
            System.out.println(accessToken);

            // 2. 해당 UserToken으로 Calendar내역을 각각 가져온다
            Event event = calendarService.getMyCalendar(accessToken, "primary");
            String eventInTodayList = getUserEventInToday(event);

            System.out.println(eventInTodayList);

//            saveRedisSummeryCalendar(eventInTodayList);

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
    public void  getSummeryCalendarFromGPT(List<Event.Item> eventList){



    }
    public void saveRedisSummeryCalendar(String summeryText){

        RedisSummeryCalendar summeryCalendar = RedisSummeryCalendar.builder()
                .summeryCalendar(summeryText)
                .build();

        redisSummeryCalendarRepository.save(summeryCalendar);
    }



}
