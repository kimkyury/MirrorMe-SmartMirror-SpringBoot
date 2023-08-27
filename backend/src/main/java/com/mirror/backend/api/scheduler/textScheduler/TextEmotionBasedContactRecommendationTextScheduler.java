package com.mirror.backend.api.scheduler.textScheduler;


import com.mirror.backend.api.dto.UserDto;
import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.entity.GoogleOAuthToken;
import com.mirror.backend.api.entity.TextEmotionBasedContactRecommendation;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.repository.ConnectUserRepository;
import com.mirror.backend.api.repository.GoogleOAuthTokenRepository;
import com.mirror.backend.api.repository.TextEmotionBasedContactRecommendationRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.impl.EmotionServiceImpl;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.Iterator;
import java.util.List;

@Component
@RequiredArgsConstructor
public class TextEmotionBasedContactRecommendationTextScheduler implements TextSchedulerHandler {

    private final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    private final TextEmotionBasedContactRecommendationRepository textEmotionBasedContactRecommendationRepository;
    private final UserRepository userRepository;
    private final ConnectUserRepository connectUserRepository;

    private final OAuthService oAuthService;
    private final EmotionServiceImpl emotionService;

    private final TokenUtil tokenUtil;

    private TextSchedulerHandler nextHandler;

    @Override
    public void setNextHandler(TextSchedulerHandler next){
        this.nextHandler = next;
    }

    @Override
    public void execute(){
        System.out.println("------------Scheduler: EmotionBased Contact Recommendation ----------");

        Iterable<GoogleOAuthToken> googleOAuthToken = googleOAuthTokenRepository.findAll();
        Iterator<GoogleOAuthToken> iterator = googleOAuthToken.iterator();

        while (iterator.hasNext()) {

            String userEmail = TextSchedulerHandler.getUserStringUseOAuthToken(iterator.next(), tokenUtil);
            User user = userRepository.findByUserEmail(userEmail).get();
            List<UserDto> angryResList =  emotionService.familyAngryList(user.getUserId());

            for(UserDto angryUser : angryResList){
                ConnectUser connectUserInfo = connectUserRepository.findByIdUserIdAndIdConnectUserId(
                        user.getUserId(), angryUser.getUserId()).get();
                String angryUserAlias = connectUserInfo.getConnectUserAlias();

                String text = getTextEmotionBasedContactRecommendation(user.getUserName(), angryUserAlias);
                saveTextEmotionBasedContactRecommendationToRedis(userEmail, text);
            }
        }

        System.out.println("------------ Finish Scheduler ----------");

        if ( nextHandler != null){
            nextHandler.execute();
        }
    }

    private String getTextEmotionBasedContactRecommendation(String userName, String angryUserAlias){

        StringBuilder sb = new StringBuilder();
        sb.append(userName).append("님, ")
                .append("어제 ").append(angryUserAlias).append("님의 기분이 안 좋아보이셨어요. ")
                .append("연락해 보시는 건 어떠세요?");

        return sb.toString();
    }

    private  void saveTextEmotionBasedContactRecommendationToRedis(String userEmail, String text){

        TextEmotionBasedContactRecommendation textEmotionBasedContactRecommendation = TextEmotionBasedContactRecommendation.builder()
                .userEmail(userEmail)
                .textEmotionBasedContactRecommendation(text)
                .targetDay(EtcUtil.getTodayYYYYMMDD())
                .build();

        textEmotionBasedContactRecommendationRepository.save(textEmotionBasedContactRecommendation);
    }
}
