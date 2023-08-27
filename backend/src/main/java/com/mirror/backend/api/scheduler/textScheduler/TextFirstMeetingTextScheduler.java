package com.mirror.backend.api.scheduler.textScheduler;


import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.Iterator;
import java.util.Optional;

@Component
@RequiredArgsConstructor
public class TextFirstMeetingTextScheduler implements TextSchedulerHandler {

    private final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    private final TextSummaryScheduleRepository textSummaryScheduleRepository;
    private final TextFamilyBirthdayRepository textFamilyBirthdayRepository;
    private final TextCautionRainyRepository textCautionRainyRepository;
    private final TextFirstMeetingRepository textFirstMeetingRepository;
    private final TextVideoViewRepository textVideoViewRepository;
    private final TextEmotionBasedContactRecommendationRepository textEmotionBasedContactRecommendationRepository;
    private final UserRepository userRepository;

    private final TokenUtil tokenUtil;

    private TextSchedulerHandler nextHandler;

    @Override
    public void setNextHandler(TextSchedulerHandler next){
        this.nextHandler = next;
    }

    @Override
    public void execute(){
        System.out.println("------------Scheduler: First Text----------");
        // redis내의 유저 Token을 가져온다
        Iterable<GoogleOAuthToken> googleOauthToken= googleOAuthTokenRepository.findAll();
        Iterator<GoogleOAuthToken> iterator = googleOauthToken.iterator();

        while(iterator.hasNext()){

            String userEmail = TextSchedulerHandler.getUserStringUseOAuthToken(iterator.next(), tokenUtil);
            User user = userRepository.findByUserEmail(userEmail).get();
            Long userHouseholdId = user.getHousehold().getHouseholdId();

            String today = EtcUtil.getTodayYYYYMMDD();

            // 미열람 VideoMessage가 있는지 확인한다
            Optional<TextVideoView> textVideoViewOptional = textVideoViewRepository.findById(userEmail);
            if (textVideoViewOptional.isPresent() && textVideoViewOptional.get().getTargetDay().equals(today)){
                saveRedisFirstText("0401", textVideoViewOptional.get().getTextVideoView(), userEmail);
                continue;
            }

            // 해당 유저의 친인척 중 전날에 화가 나있던 사람이 있는지 확인한다
            Optional<TextEmotionBasedContactRecommendation> textEmotionBasedContactRecommendation =
                    textEmotionBasedContactRecommendationRepository.findById(userEmail);
            if (textEmotionBasedContactRecommendation.isPresent() && textEmotionBasedContactRecommendation.get().getTargetDay().equals(today) ){
                saveRedisFirstText("0402", textEmotionBasedContactRecommendation.get()
                        .getTextEmotionBasedContactRecommendation(), userEmail);
                continue;
            }

            // 해당 유저의 친인척의 생일 정보가 있는지 확인한다
            Optional<TextFamilyBirthday> textFamilyBirthdayOptional = textFamilyBirthdayRepository.findById(userEmail);
            if ( textFamilyBirthdayOptional.isPresent() && textFamilyBirthdayOptional.get().getTargetDay().equals(today)){
                saveRedisFirstText("0202", textFamilyBirthdayOptional.get().getTextFamilyBirthday(), userEmail);
                continue;
            }

            // 오늘 기준의 날씨 기상정보에서 비가 오는지 확인한다
            TextCautionRainy textCautionRainy = textCautionRainyRepository.findById(String.valueOf(userHouseholdId)).get();
            if (textCautionRainy.getIsRainyCode().equals(String.valueOf(1))){
                saveRedisFirstText("0101", textCautionRainy.getTextCautionRainy(), userEmail);
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

        if ( nextHandler != null){
            nextHandler.execute();
        }
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
