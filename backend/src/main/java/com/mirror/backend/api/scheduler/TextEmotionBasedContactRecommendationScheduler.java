package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.dto.UserDto;
import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.entity.GoogleOAuthToken;
import com.mirror.backend.api.entity.TextEmotionBasedContactRecommendation;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.api.service.EmotionService;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.impl.EmotionServiceImpl;
import com.mirror.backend.api.service.impl.VideoServiceImpl;
import com.mirror.backend.common.utils.ChatGptUtil;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.Iterator;
import java.util.List;

@Component
@RequiredArgsConstructor
public class TextEmotionBasedContactRecommendationScheduler {

    public final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    public final TextEmotionBasedContactRecommendationRepository textEmotionBasedContactRecommendationRepository;
    public final UserRepository userRepository;
    public final ConnectUserRepository connectUserRepository;

    public final OAuthService oAuthService;
    public final EmotionServiceImpl emotionService;

    public final ChatGptUtil chatGptUtil;
    public final TokenUtil tokenUtil;

    @Scheduled(cron = "0 * * * * ?")   // Develop
//    @Scheduled(cron = "0 0 0 * * ?") // Distribution
    public void fetchRedisData() {

        System.out.println("------------Scheduler: EmotionBased Contact Recommendation ----------");

        Iterable<GoogleOAuthToken> googleOAuthToken = googleOAuthTokenRepository.findAll();
        Iterator<GoogleOAuthToken> iterator = googleOAuthToken.iterator();

        while (iterator.hasNext()) {

            String userEmail = getUserEmailUseGoogleOAuthToken(iterator);
            User user = userRepository.findByUserEmail(userEmail).get();
            Long userId = user.getUserId();
            List<UserDto> angryResList =  emotionService.familyAngryList(userId);

            for(UserDto angryUser : angryResList){

                ConnectUser connectUserInfo = connectUserRepository.findByIdUserIdAndIdConnectUserId(
                        userId, angryUser.getUserId()).get();
                String angryUserAlias = connectUserInfo.getConnectUserAlias();

                String text = getTextEmotionBasedContactRecommendation(user.getUserName(), angryUserAlias);
                saveTextEmotionBasedContactRecommendationToRedis(userEmail, text);
            }
        }

        System.out.println("------------ Finish Scheduler ----------");
    }

    public String  getUserEmailUseGoogleOAuthToken(Iterator<GoogleOAuthToken> iterator){

        GoogleOAuthToken userTokenInfo = iterator.next();
        String accessToken = userTokenInfo.getAccessToken();
        String refreshToken = userTokenInfo.getRefreshToken();
        accessToken = tokenUtil.confirmAccessToken(accessToken, refreshToken);
        String userEmail = oAuthService.getUserEmailFromAccessToken(accessToken);

        return userEmail;
    }

    public String getTextEmotionBasedContactRecommendation(String userName, String angryUserAlias){

        StringBuilder sb = new StringBuilder();
        sb.append(userName).append("님, ")
                .append("어제 ").append(angryUserAlias).append("님의 기분이 안 좋아보이셨어요. ")
                .append("연락해 보시는 건 어떠세요?");

        return sb.toString();
    }

    public  void saveTextEmotionBasedContactRecommendationToRedis(String userEmail, String text){

        TextEmotionBasedContactRecommendation textEmotionBasedContactRecommendation = TextEmotionBasedContactRecommendation.builder()
                .userEmail(userEmail)
                .textEmotionBasedContactRecommendation(text)
                .targetDay(EtcUtil.getTodayYYYYMMDD())
                .build();

        textEmotionBasedContactRecommendationRepository.save(textEmotionBasedContactRecommendation);
    }
}
