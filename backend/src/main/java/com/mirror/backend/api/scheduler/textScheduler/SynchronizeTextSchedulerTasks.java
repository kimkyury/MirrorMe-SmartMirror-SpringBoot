package com.mirror.backend.api.scheduler.textScheduler;

import com.mirror.backend.api.repository.*;
import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.impl.EmotionServiceImpl;
import com.mirror.backend.api.service.impl.VideoServiceImpl;
import com.mirror.backend.common.utils.ChatGptUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class SynchronizeTextSchedulerTasks {

    private final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    private final TextSummaryScheduleRepository textSummaryScheduleRepository;
    private final TextFamilyBirthdayRepository familyBirthdayRepository;
    private final TextEmotionBasedContactRecommendationRepository textEmotionBasedContactRecommendationRepository;
    private final TextCautionRainyRepository textCautionRainyRepository;
    private final TextFirstMeetingRepository textFirstMeetingRepository;
    private final TextVideoViewRepository textVideoViewRepository;
    private final ConnectUserRepository connectUserRepository;
    private final UserRepository userRepository;

    private final CalendarService calendarService;
    private final OAuthService oAuthService;
    private final EmotionServiceImpl emotionService;
    private final VideoServiceImpl videoService;

    private final ChatGptUtil chatGptUtil;
    private final TokenUtil tokenUtil;

    @Scheduled(cron = "0 9 * * * ?") // Develop
//    @Scheduled(cron = "0 0 0 * * ?") // Deploy
    private void midnightJob(){

        TextSchedulerHandler firstScheduler = new TextSummaryCalendarTextScheduler(googleOAuthTokenRepository,
                textSummaryScheduleRepository, calendarService, oAuthService, chatGptUtil, tokenUtil);
        TextSchedulerHandler secondScheduler = new TextFamilyBirthdayTextScheduler(googleOAuthTokenRepository,
                familyBirthdayRepository, connectUserRepository, userRepository, calendarService,
                oAuthService, chatGptUtil, tokenUtil);
        TextSchedulerHandler thirdScheduler = new TextEmotionBasedContactRecommendationTextScheduler(googleOAuthTokenRepository,
                textEmotionBasedContactRecommendationRepository, userRepository, connectUserRepository, oAuthService, emotionService, tokenUtil);
        TextSchedulerHandler fourthScheduler = new TextVideoViewTextScheduler(googleOAuthTokenRepository, textVideoViewRepository, userRepository,
                connectUserRepository, oAuthService, videoService, tokenUtil);
        TextSchedulerHandler fifthScheduler = new TextFirstMeetingTextScheduler(googleOAuthTokenRepository, textSummaryScheduleRepository,
                familyBirthdayRepository, textCautionRainyRepository, textFirstMeetingRepository, textVideoViewRepository, textEmotionBasedContactRecommendationRepository,
                userRepository, tokenUtil);

        firstScheduler.setNextHandler(secondScheduler);
        secondScheduler.setNextHandler(thirdScheduler);
        thirdScheduler.setNextHandler(fourthScheduler);
        fourthScheduler.setNextHandler(fifthScheduler);

        System.out.println("------------ 동기 스케쥴러 실행 시작-----------");
        firstScheduler.execute();
        System.out.println("------------ 동기 스케쥴러 실행 끝-----------");
    }
}
