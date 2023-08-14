package com.mirror.backend.api.scheduler.textScheduler;

import com.mirror.backend.api.entity.GoogleOAuthToken;
import com.mirror.backend.common.utils.TokenUtil;


public interface TextSchedulerHandler {

    void setNextHandler(TextSchedulerHandler next);
    void execute();

    static String getUserStringUseOAuthToken(GoogleOAuthToken userTokenInfo, TokenUtil tokenUtil){

        String accessToken = userTokenInfo.getAccessToken();
        String refreshToken = userTokenInfo.getRefreshToken();
        accessToken = tokenUtil.confirmAccessToken(accessToken, refreshToken);

        return accessToken;
    }
}
