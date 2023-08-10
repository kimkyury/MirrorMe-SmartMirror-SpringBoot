package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.common.utils.ChatGptUtil;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.cache.CacheProperties;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import springfox.documentation.service.OAuth;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Iterator;
import java.util.Optional;

@Component
@RequiredArgsConstructor
public class MirrorFirstTextScheduler {

    public final RedisUserTokenRepository redisUserTokenRepository;
    public final RedisSummeryCalendarRepository redisSummeryCalendarRepository;
    public final RedisFamilyBirthdayRepository redisFamilyBirthdayRepository;
    public final RedisIsRainyRepository redisIsRainyRepository;
    public final RedisFirstMirrorTextRepository redisFirstMirrorTextRepository;
    public final UserRepository userRepository;

    public final TokenUtil tokenUtil;
    public final OAuthService oAuthService;


//    @Scheduled(cron = "0 * * * * ?") // 개발용
    @Scheduled(cron = "5 0 0 * * ?") // 배용, 매일 자정 5분마다 실행 ( 이전 것들이 다 실행되고 찾을 수 있게)
    public void fetchRedisData() {
        System.out.println("------------First Text Scheduler----------");
        // redis내의 유저 Token을 가져온다
        Iterable<RedisUserToken> redisUserTokenIterable= redisUserTokenRepository.findAll();
        Iterator<RedisUserToken> iterator = redisUserTokenIterable.iterator();

        while(iterator.hasNext()){
            RedisUserToken userTokenInfo = iterator.next();
            String accessToken = userTokenInfo.getAccessToken();
            String refreshToken = userTokenInfo.getRefreshToken();

            // AccessToken의 유효성 검사, 만약 불일치시 재발급
            accessToken = tokenUtil.confirmAccessToken(accessToken, refreshToken);
            String userEmail = oAuthService.getUserEmailFromAccessToken(accessToken);
            User user = userRepository.findByUserEmail(userEmail).get();
            Long userHouseholdId = user.getHousehold().getHouseholdId();

            System.out.println(userEmail);

            // 오늘 기준의 데이터를 찾는다
            String today = EtcUtil.getTodayYYYYMMDD();

            // 오늘 기준의 날씨 기상정보에서 비가 오는지 확인한다
            RedisIsRainy redisIsRainy = redisIsRainyRepository.findById(String.valueOf(userHouseholdId)).get();
            if (redisIsRainy.getIsRainyCode().equals(String.valueOf(1))){
                saveRedisFirstText("0101", redisIsRainy.getIsRainyText(), userEmail);
                continue;
            }

            // 해당 유저의 친인척의 생일 정보가 있는지 확인한다
            Optional<RedisFamilyBirthday> redisFamilyBirthdayOptional = redisFamilyBirthdayRepository.findById(userEmail);
            if ( redisFamilyBirthdayOptional.isPresent() && redisFamilyBirthdayOptional.get().getTargetDay().equals(today)){
                saveRedisFirstText("0202", redisFamilyBirthdayOptional.get().getFamilyBirthday(), userEmail);
                continue;
            }

            // 해당 유저의 3줄 요약 정보가 있는지 확인한다
            Optional<RedisSummeryCalendar> redisSummeryCalendar = redisSummeryCalendarRepository.findById(userEmail);
            if (redisSummeryCalendar.isPresent() && redisSummeryCalendar.get().getTargetDay().equals(today)){
                saveRedisFirstText("0301", redisSummeryCalendar.get().getSummeryCalendar(), userEmail);
                continue;
            }
        }

    }

    private void saveRedisFirstText(String textCode, String isRainyText, String  userEmail) {
        RedisMirrorFirstText redisFirstMirrorText = RedisMirrorFirstText.builder()
                .userEmail(userEmail)
                .textContent(isRainyText)
                .textCode(textCode)
                .isUsed("0")
                .build();

        redisFirstMirrorTextRepository.save(redisFirstMirrorText);
    }



}
