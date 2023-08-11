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
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;

@Component
@RequiredArgsConstructor
public class FmailyBirthDayScheduler {

    public final RedisUserTokenRepository redisUserTokenRepository;
    public final RedisSummeryCalendarRepository redisSummeryCalendarRepository;
    public final CalendarService calendarService;
    public final ChatGptUtil chatGptUtil;
    public final OAuthService oAuthService;
    public final TokenUtil tokenUtil;
    public final RedisFamilyBirthdayRepository redisFamilyBirthdayRepository;
    public final ConnectUserRepository connectUserRepository;
    public final UserRepository userRepository;



    // 1. Redis내의 유저 Token들을 모두 가져온다
//    @Scheduled(cron = "0 * * * * ?")   // 개발용, 매분 0초마다 실행
    @Scheduled(cron = "0 1 0 * * ?") // 배포용, 매일 자정마다 실행
    public void fetchRedisData() {
        System.out.println("------------FamilyBirthDay Recommend Present Scheduler----------");
        // redis내의 유저 Token을 가져온다
        Iterable<RedisUserToken> redisUserTokenIterable= redisUserTokenRepository.findAll();
        Iterator<RedisUserToken> iterator = redisUserTokenIterable.iterator();


        while (iterator.hasNext()) {

            RedisUserToken userTokenInfo = iterator.next();

            String accessToken = userTokenInfo.getAccessToken();
            String refreshToken = userTokenInfo.getRefreshToken();

            // AccessToken의 유효성 검사, 만약 불일치시 재발급
            accessToken = tokenUtil.confirmAccessToken(accessToken, refreshToken);

            // 해당 유저의 Email을 조회
            String userEmail = oAuthService.getUserEmailFromAccessToken(accessToken);
            Long userId = userRepository.findByUserEmail(userEmail).get().getUserId();

            // 해당 유저의 친인척 중 생일인 사람이 있는지 조회
            List<ConnectUser> connectUsers = connectUserRepository.findByIdUserId(userId);
            List<Long> connectUserIds = connectUsers.stream().map(c -> c.getConnectUser().getUserId()).collect(Collectors.toList());
            List<User> todayBirthUser= userRepository.findByBirthdayAndUserIdIn(EtcUtil.getTodayYYYYMMDD(), connectUserIds);
            System.out.print(todayBirthUser);

            // 생일인 유저가 특정한 일이 있는지 GPT에게 정리해달라고 하기

            for( User user : todayBirthUser){

                RedisUserToken birthUserToken = redisUserTokenRepository.findById(user.getUserEmail()).get();
                String birthUserAccessToken = birthUserToken.getAccessToken();
                String birthUserRefreshToken = birthUserToken.getRefreshToken();

                // AccessToken의 유효성 검사, 만약 불일치시 재발급
                accessToken = tokenUtil.confirmAccessToken(birthUserAccessToken, birthUserRefreshToken);

                // 오늘 이후로 birthDayUser의 일정들을 다 조회해봄
                Event event = calendarService.getMyCalendar(accessToken, "primary");
                String birthUserEventInFuture = getUserAllEventFuture(event);

                // GPT에게 이런 사람에게 어떤 선물이 좋겠는지 이유와 함께 물어봄
                String answer = getRecommendPresentFromGPT(birthUserEventInFuture);
                System.out.println(answer);
                saveRedisFamilyBirthday(answer, userEmail, user.getUserName());
            }
        }
    }

    public String getUserAllEventFuture(Event event){
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

            // 오늘이 시작날짜보다 전이면서, 오늘이 끝나는 날짜를 지난 것도 아닌.
            boolean chk = now.isBefore(startDate) && !now.isAfter(endDate);
            if (chk) sb.append(item.getSummary() +", ");
        }

        userEventList = sb.toString();
        return userEventList;

    }

    // 3. 해당 Calendar내역을 3줄 요약하도록 GPT한테 요청한다
    public String  getRecommendPresentFromGPT(String birthUserEventInFuture){

        StringBuilder sb = new StringBuilder();
        sb.append("다음과 같은 일정들이 있습니다. 이런 사람은 어떤 선물이 필요할까요?");
        sb.append("최대한 간략하게 한가지만 추천해주세요. 또한 이유도 설명해주세요. (대답이 한글 기준 20자가 넘지않도록) ");
        sb.append("대답 형식은 다음과 같이 부탁드립니다. '{선물}을 준비해보시는게 어떠세요? 이런 일정이 있거든요!");
        sb.append(" // " + birthUserEventInFuture + " // ");
        String answer = chatGptUtil.createMessage(sb.toString());
        return answer;

    }

    public void saveRedisFamilyBirthday(String recommendPresnet, String userEmail, String birthDayUserName){

        StringBuilder sb = new StringBuilder();
        sb.append("안녕하세요!, 오늘은 " )
                .append( birthDayUserName)
                .append("의 생일이네요. ")
                .append(recommendPresnet);


        RedisFamilyBirthday redisFamilyBirthday = RedisFamilyBirthday.builder()
                .userEmail(userEmail)
                .familyBirthday(sb.toString())
                .targetDay(EtcUtil.getTodayYYYYMMDD())
                .build();

        redisFamilyBirthdayRepository.save(redisFamilyBirthday);
    }


}
