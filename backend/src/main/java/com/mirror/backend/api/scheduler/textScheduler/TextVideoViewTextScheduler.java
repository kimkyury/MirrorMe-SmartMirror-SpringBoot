package com.mirror.backend.api.scheduler.textScheduler;


import com.mirror.backend.api.dto.MessageDto;
import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.entity.GoogleOAuthToken;
import com.mirror.backend.api.entity.TextVideoView;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.repository.ConnectUserRepository;
import com.mirror.backend.api.repository.GoogleOAuthTokenRepository;
import com.mirror.backend.api.repository.TextVideoViewRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.impl.VideoServiceImpl;
import com.mirror.backend.common.utils.EtcUtil;
import com.mirror.backend.common.utils.TokenUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.Iterator;
import java.util.List;

@Component
@RequiredArgsConstructor
public class TextVideoViewTextScheduler implements TextSchedulerHandler {

    private final GoogleOAuthTokenRepository googleOAuthTokenRepository;
    private final TextVideoViewRepository textVideoViewRepository;
    private final UserRepository userRepository;
    private final ConnectUserRepository connectUserRepository;

    private final OAuthService oAuthService;
    private final VideoServiceImpl videoService;

    private final TokenUtil tokenUtil;

    private TextSchedulerHandler nextHandler;

    @Override
    public void setNextHandler(TextSchedulerHandler next){
        this.nextHandler = next;
    }

    @Override
    public void execute(){

        System.out.println("------------Scheduler: Video View Calendar----------");

        Iterable<GoogleOAuthToken> googleOAuthToken = googleOAuthTokenRepository.findAll();
        Iterator<GoogleOAuthToken> iterator = googleOAuthToken.iterator();

        while (iterator.hasNext()) {

            String accessToken = TextSchedulerHandler.getUserStringUseOAuthToken(iterator.next(), tokenUtil);
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

        if ( nextHandler != null){
            nextHandler.execute();
        }
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
