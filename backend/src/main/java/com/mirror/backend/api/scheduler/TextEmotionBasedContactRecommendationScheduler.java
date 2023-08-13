package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.entity.GoogleOAuthToken;
import com.mirror.backend.api.repository.GoogleOAuthTokenRepository;
import com.mirror.backend.api.repository.TextVideoViewRepository;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.impl.VideoServiceImpl;
import com.mirror.backend.common.utils.ChatGptUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.Iterator;

@Component
@RequiredArgsConstructor
public class TextEmotionBasedContactRecommendationScheduler {

    public final GoogleOAuthTokenRepository googleOAuthTokenRepository;

    public final OAuthService oAuthService;

    public final ChatGptUtil chatGptUtil;
    public final TokenUtil tokenUtil;

//    @Scheduled(cron = "0 * * * * ?")   // 개발용, 매분 0초마다 실행
    @Scheduled(cron = "0 0 0 * * ?") // 배용, 매일 자정마다 실행
    public void fetchRedisData() {

        System.out.println("------------Scheduler: Video View Calendar----------");

        Iterable<GoogleOAuthToken> googleOAuthToken = googleOAuthTokenRepository.findAll();
        Iterator<GoogleOAuthToken> iterator = googleOAuthToken.iterator();

        while (iterator.hasNext()) {
            GoogleOAuthToken userTokenInfo = iterator.next();

            String accessToken = userTokenInfo.getAccessToken();
            String refreshToken = userTokenInfo.getRefreshToken();

            // AccessToken의 유효성 검사, 만약 불일치시 재발급
            accessToken = tokenUtil.confirmAccessToken(accessToken, refreshToken);

            // 1. 해당 유저의 이메일을 가져온다
            String userEmail = oAuthService.getUserEmailFromAccessToken(accessToken);

            // 2. ResponseVideoList를 가져온다 (videoService)

            // 3. 해당 List가 존재한다면, 열람해보겠냐는 질문이 담긴 텍스트를 보낸다

            // 4. 해당 Text를 Redis에 저장한다

        }
        System.out.println("------------ Finish Scheduler ----------");
    }



}
