package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.Iterator;
import java.util.Optional;

@Component
@RequiredArgsConstructor
public class TextFirstMeetingScheduler {

    public final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    public final TextSummaryScheduleRepository textSummaryScheduleRepository;
    public final TextFamilyBirthdayRepository textFamilyBirthdayRepository;
    public final TextCautionRainyRepository textCautionRainyRepository;
    public final TextFirstMeetingRepository textFirstMeetingRepository;
    public final UserRepository userRepository;

    public final TokenUtil tokenUtil;
    public final OAuthService oAuthService;

//    @Scheduled(cron = "0 * * * * ?") // 개발용
    @Scheduled(cron = "0 5 0 * * ?") // 배용, 매일 자정 5분마다 실행 ( 이전 것들이 다 실행되고 찾을 수 있게)
    public void fetchRedisData() {
        System.out.println("------------Scheduler: First Text----------");
        // redis내의 유저 Token을 가져온다
        Iterable<GoogleOAuthToken> googleOauthToken= googleOAuthTokenRepository.findAll();
        Iterator<GoogleOAuthToken> iterator = googleOauthToken.iterator();

        while(iterator.hasNext()){
            GoogleOAuthToken userTokenInfo = iterator.next();
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
            TextCautionRainy textCautionRainy = textCautionRainyRepository.findById(String.valueOf(userHouseholdId)).get();
            if (textCautionRainy.getIsRainyCode().equals(String.valueOf(1))){
                saveRedisFirstText("0101", textCautionRainy.getTextCautionRainy(), userEmail);
                continue;
            }

            // 해당 유저의 친인척의 생일 정보가 있는지 확인한다
            Optional<TextFamilyBirthday> textFamilyBirthdayOptional = textFamilyBirthdayRepository.findById(userEmail);
            if ( textFamilyBirthdayOptional.isPresent() && textFamilyBirthdayOptional.get().getTargetDay().equals(today)){
                saveRedisFirstText("0202", textFamilyBirthdayOptional.get().getTextFamilyBirthday(), userEmail);
                continue;
            }

            // 해당 유저의 3줄 요약 정보가 있는지 확인한다
            Optional<TextSummarySchedule> textSumaryScheduleOptional = textSummaryScheduleRepository.findById(userEmail);
            if (textSumaryScheduleOptional.isPresent() && textSumaryScheduleOptional.get().getTargetDay().equals(today)){
                saveRedisFirstText("0301", textSumaryScheduleOptional.get().getTextSummarySchedule(), userEmail);
                continue;
            }
        }
        System.out.println("------------ Finish Scheduler ----------");
    }

    private void saveRedisFirstText(String textCode, String isRainyText, String  userEmail) {
        TextFirstMeeting testFirstMeeting = TextFirstMeeting.builder()
                .userEmail(userEmail)
                .textContent(isRainyText)
                .textCode(textCode)
                .isUsed("0")
                .build();

        textFirstMeetingRepository.save(testFirstMeeting);
    }



}
