package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.dto.MessageDto;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.impl.VideoServiceImpl;
import com.mirror.backend.common.utils.ChatGptUtil;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Iterator;
import java.util.List;

@Component
@RequiredArgsConstructor
public class TextVideoViewScheduler {

    public final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    public final TextVideoViewRepository textVideoViewRepository;
    public final UserRepository userRepository;
    public final ConnectUserRepository connectUserRepository;

    public final OAuthService oAuthService;
    public final VideoServiceImpl videoService;

    public final ChatGptUtil chatGptUtil;
    public final TokenUtil tokenUtil;

//    @Scheduled(cron = "0 * * * * ?")   // develop
    @Scheduled(cron = "0 5 0 * * ?") // deploy
    public void fetchRedisData() {

        System.out.println("------------Scheduler: Video View Calendar----------");

        Iterable<GoogleOAuthToken> googleOAuthToken = googleOAuthTokenRepository.findAll();
        Iterator<GoogleOAuthToken> iterator = googleOAuthToken.iterator();

        while (iterator.hasNext()) {
            GoogleOAuthToken userTokenInfo = iterator.next();

            String accessToken = userTokenInfo.getAccessToken();
            String refreshToken = userTokenInfo.getRefreshToken();

            accessToken = tokenUtil.confirmAccessToken(accessToken, refreshToken); // AccessToken Check & ReIssue
            String receiveUserEmail = oAuthService.getUserEmailFromAccessToken(accessToken);
            List<MessageDto.ResponseMessageDetail>  responseMessageDetailList = videoService.unReadMessageList(receiveUserEmail);

            if ( responseMessageDetailList.size() > 0){
                User receiveUser =  userRepository.findByUserEmail(receiveUserEmail).get();
                String receiveUserName = receiveUser.getUserName();
                Long receiveUserId = receiveUser.getUserId();

                // TODO: 한 명에 대해서만 작동.
                for(MessageDto.ResponseMessageDetail responseMessageDetail : responseMessageDetailList){

                    Long sendUserId = userRepository.findByUserEmail(responseMessageDetail.getSendUserEmail()).get().getUserId();
                    ConnectUser sendUserAliasInfo =  connectUserRepository.findByIdUserIdAndIdConnectUserId(receiveUserId, sendUserId).get();
                    String sendUserAlias = sendUserAliasInfo.getConnectUserAlias();
                    String textVideoView = getTextVideoView(receiveUserName, sendUserAlias);

                    saveTextVideoViewToRedis(receiveUserEmail, sendUserId, textVideoView);
                }
            }
        }

        System.out.println("------------ Finish Scheduler ----------");
    }


    public String getTextVideoView(String receiveUserName, String sendUserName){

        StringBuilder sb = new StringBuilder();
        sb.append("안녕하세요! ").append(receiveUserName).append("님, ")
                .append(sendUserName).append("님이 영상메세지를 남겼네요. 확인해보시겠어요?");

        return sb.toString();
    }

    public void saveTextVideoViewToRedis(String receiveUserEmail, Long sendUserId,  String text){

        TextVideoView textVideoView = TextVideoView.builder()
                .userEmail(receiveUserEmail)
                .senderUserId(String.valueOf(sendUserId))
                .textVideoView(text)
                .targetDay(EtcUtil.getTodayYYYYMMDD())
                .build();

        textVideoViewRepository.save(textVideoView);
    }
}
