package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.common.utils.ChatGptUtil;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

@Component
@RequiredArgsConstructor
public class TextFamilyBirthdayScheduler {

    public final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    public final TextFamilyBirthdayRepository textFamilyBirthdayRepository;
    public final ConnectUserRepository connectUserRepository;
    public final UserRepository userRepository;

    public final CalendarService calendarService;
    public final OAuthService oAuthService;

    public final ChatGptUtil chatGptUtil;
    public final TokenUtil tokenUtil;

//    @Scheduled(cron = "0 * * * * ?")   // Develop
    @Scheduled(cron = "0 3 0 * * ?") // deploy
    public void fetchRedisData() {
        System.out.println("------------Scheduler: FamilyBirthDay Recommend Present----------");

        // Today + (1 ~ 7) later Birthday
        List<String> upcomingBirthdayLists = getUpcomingBirthdays();
        List<User> upcomingBirthdayUserAllList = new ArrayList<>();

        for (String birthday : upcomingBirthdayLists) {
            List<User> birthdayUserList = userRepository.findByBirthday(birthday);
            upcomingBirthdayUserAllList.addAll(birthdayUserList);
        }

        System.out.println(upcomingBirthdayUserAllList);

        for (User birthdayUser : upcomingBirthdayUserAllList) {
            String birthdayUserAllUpcomingEvents = getBirthDayUserUpcomingEventsProcedure(birthdayUser);
            String gptAnswer = getRecommendPresentFromGPT(birthdayUserAllUpcomingEvents);     // Request PresentRecommend to GPT
            List<ConnectUser> birthUserConnectUser = connectUserRepository.findByIdUserId(birthdayUser.getUserId());

            for (ConnectUser connectUser : birthUserConnectUser) {
                System.out.println(connectUser.getId().getConnectUserId() + " " + birthdayUser.getUserId());
                ConnectUser aliasInfo = connectUserRepository.findByIdUserIdAndIdConnectUserId(connectUser.getId().getConnectUserId() , birthdayUser.getUserId()).get();
                saveRedisUpcomingFamilyBirthday(gptAnswer, connectUser.getConnectUser().getUserEmail(), aliasInfo.getConnectUserAlias());
            }
        }

        // Today Birthday
        List<User> todayBirthUserList = userRepository.findByBirthday(EtcUtil.getTodayMMDD());
        System.out.println(todayBirthUserList);
        if (todayBirthUserList.size() != 0) {
            for (User todayBirthUser : todayBirthUserList) {
                String birthdayUserAllUpcomingEvents = getBirthDayUserUpcomingEventsProcedure(todayBirthUser);
                String gptAnswer = getRecommendPresentFromGPT(birthdayUserAllUpcomingEvents); // Request PresentRecommend to GPT
                List<ConnectUser> birthUserConnectUser = connectUserRepository.findByIdUserId(todayBirthUser.getUserId());

                for (ConnectUser connectUser : birthUserConnectUser) {
                    ConnectUser aliasInfo = connectUserRepository.findByIdUserIdAndIdConnectUserId(connectUser.getId().getConnectUserId(), todayBirthUser.getUserId()).get();
                    saveRedisFamilyBirthday(gptAnswer, connectUser.getConnectUser().getUserEmail(), aliasInfo.getConnectUserAlias());
                }
            }
        }

        System.out.println("------------ Finish Scheduler ----------");
    }

    private String getBirthDayUserUpcomingEventsProcedure(User todayBirthUser) {
        // 1. User의 Token 찾아오기
        GoogleOAuthToken birthUserToken = googleOAuthTokenRepository.findById(todayBirthUser.getUserEmail()).get();
        String accessToken = birthUserToken.getAccessToken();
        String refreshToken = birthUserToken.getRefreshToken();

        // 2. AccessToken 유효한지 확인하여 재발급받기
        accessToken = tokenUtil.confirmAccessToken(accessToken, refreshToken);

        // 3. User의 앞으로의 6개월 이내 이벤트 갖고오기
        String userAllUpcomingEvents = getUserAllUpcomingEventsWithinSixMonth(accessToken);

        return userAllUpcomingEvents;
    }

    private List<String> getUpcomingBirthdays(){

        List<String> birthdays = new ArrayList<>();
        LocalDate today = LocalDate.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMdd");

        for (int i = 1; i <= 7; i++) {
            LocalDate nextDate = today.plusDays(i);
            birthdays.add(nextDate.format(formatter));
        }

        return birthdays;
    }

    public String getUserAllUpcomingEventsWithinSixMonth(String accessToken){

        Event event = calendarService.getMyCalendar(accessToken, "primary");

        String userEventList;
        StringBuilder sb = new StringBuilder();
        LocalDate now = LocalDate.now();
        for( Event.Item item: event.getItems()) {
            String startTime = item.getStart().getDateTime(); // 시작날짜
            String endTime = item.getEnd().getDateTime(); // 종료날짜
            startTime = startTime == null ? item.getStart().getDate() : startTime.substring(0, 10);
            endTime = endTime == null ? item.getEnd().getDate() : endTime.substring(0, 10);

            DateTimeFormatter parser = DateTimeFormatter.ofPattern("yyyy-MM-dd");
            LocalDate startDate = LocalDate.parse(startTime, parser);
            LocalDate endDate = LocalDate.parse(endTime, parser);

            boolean chk = now.isBefore(startDate) && !now.isAfter(endDate.plusMonths(6));             // 미래 이벤트임 && 반년 이내의 이벤트임
            if (chk) sb.append(item.getSummary() +", ");
        }

        userEventList = sb.toString();

        return userEventList;
    }

    // 3. 해당 Calendar내역을 3줄 요약하도록 GPT한테 요청한다
    public String  getRecommendPresentFromGPT(String birthUserEventInFuture){

        StringBuilder sb = new StringBuilder();
        sb.append("다음과 같은 일정들이 있습니다. 이런 사람은 어떤 선물이 필요할까요?");
        sb.append(" { " + birthUserEventInFuture + " } ");
        sb.append("최대한 간략하게 한 가지 선물만 추천해주세요. 또한 이유도 설명해주세요. (대답이 한글 기준 20자가 넘지않도록) ");
        sb.append("대답 형식은 다음과 같이 부탁드립니다. '(선물)을 준비해보시는게 어떠세요? (이유가 되는 상대의 일정)이 있거든요!");
        String answer = chatGptUtil.createMessage(sb.toString());

        return answer;
    }

    public void saveRedisFamilyBirthday(String recommendPresent, String userEmail, String birthDayUserName){

        StringBuilder sb = new StringBuilder();
        sb.append("안녕하세요!, 오늘은 " )
                .append( birthDayUserName)
                .append("의 생일이네요. ")
                .append(recommendPresent);

        TextFamilyBirthday textFamilyBirthday = TextFamilyBirthday.builder()
                .userEmail(userEmail)
                .textFamilyBirthday(sb.toString())
                .targetDay(EtcUtil.getTodayYYYYMMDD())
                .build();

        textFamilyBirthdayRepository.save(textFamilyBirthday);
    }

    public void saveRedisUpcomingFamilyBirthday(String recommendPresent, String userEmail, String birthDayUserName) {

        StringBuilder sb = new StringBuilder();
        sb.append("안녕하세요!, 곧 " )
                .append( birthDayUserName)
                .append("의 생일이네요. ")
                .append(recommendPresent);

        TextFamilyBirthday textFamilyBirthday = TextFamilyBirthday.builder()
                .userEmail(userEmail)
                .textFamilyBirthday(sb.toString())
                .targetDay(EtcUtil.getTodayYYYYMMDD())
                .build();

        textFamilyBirthdayRepository.save(textFamilyBirthday);
    }
}