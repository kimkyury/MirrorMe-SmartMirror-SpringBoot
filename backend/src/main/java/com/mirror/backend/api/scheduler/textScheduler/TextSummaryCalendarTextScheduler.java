package com.mirror.backend.api.scheduler.textScheduler;


import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.entity.GoogleOAuthToken;
import com.mirror.backend.api.entity.TextSummarySchedule;
import com.mirror.backend.api.repository.GoogleOAuthTokenRepository;
import com.mirror.backend.api.repository.TextSummaryScheduleRepository;
import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.common.utils.ChatGptUtil;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Iterator;

@RequiredArgsConstructor
public class TextSummaryCalendarTextScheduler implements TextSchedulerHandler {

    private final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    private final TextSummaryScheduleRepository textSummaryScheduleRepository;

    private final CalendarService calendarService;
    private final OAuthService oAuthService;

    private final ChatGptUtil chatGptUtil;
    private final TokenUtil tokenUtil;

    private TextSchedulerHandler nextHandler;


    @Override
    public void setNextHandler(TextSchedulerHandler next){
        this.nextHandler = next;
    }

    @Override
    public void execute(){
        System.out.println("------------Scheduler: Summary Calendar Calendar----------");

        Iterable<GoogleOAuthToken> googleOAuthToken= googleOAuthTokenRepository.findAll();
        Iterator<GoogleOAuthToken> iterator = googleOAuthToken.iterator();

        while (iterator.hasNext()) {

            String accessToken = TextSchedulerHandler.getUserStringUseOAuthToken(iterator.next(), tokenUtil);
            String userEmail = oAuthService.getUserEmailFromAccessToken(accessToken);

            Event event = calendarService.getMyCalendar(accessToken, "primary");
            String eventInTodayList = getUserEventInToday(event);
            if ( eventInTodayList.equals("")){
                System.out.println("오늘 일정이 없음");
                continue;
            }

            String answer = getSummeryCalendarFromGPT(eventInTodayList);
            saveRedisSummeryCalendar(answer, userEmail);
        }

        System.out.println("------------ Finish Summary Calendar Scheduler ----------");

        if ( nextHandler != null){
            nextHandler.execute();
        }
    }

    private String getUserEventInToday(Event event){
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

    private String  getSummeryCalendarFromGPT(String eventInTodayList){

        StringBuilder sb = new StringBuilder();
        sb.append("다음과 같은 일정들이 있습니다. 가장 중요한 것 3가지를 뽑아 요약해주세요.");
        sb.append("만약 3가지보다 적다면, 있는 만큼만 나열해주세요. ");
        sb.append("각각에 대하여 1. {요약내용}, 2. {요약내용}, 3. {요약내용} 형태로 정리해주세요.");
        sb.append(" 최대한 간략하게 정리해주세요. (한글 기준 각각 10자가 넘지않도록) ");
        sb.append(" // " + eventInTodayList + " // ");

        String answer = chatGptUtil.createMessage(sb.toString());

        return answer;
    }

    public void saveRedisSummeryCalendar(String summeryText, String userEmail){

        StringBuilder sb = new StringBuilder();
        sb.append("안녕하세요!, 오늘 일정이 있어요. " );
        sb.append(summeryText);
        sb.append(", 나머지는 App에서 확인해요!");

        TextSummarySchedule textSummarySchedule = TextSummarySchedule.builder()
                .userEmail(userEmail)
                .textSummarySchedule(sb.toString())
                .targetDay(EtcUtil.getTodayYYYYMMDD())
                .build();

        textSummaryScheduleRepository.save(textSummarySchedule);
    }
}
