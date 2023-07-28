package com.mirror.backend.api.service;

import com.mirror.backend.api.entity.RedisUserToken;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import com.mirror.backend.api.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

@Service
public class OAuthService {

    @Autowired
    private UserRepository userRepository;
    @Autowired
    private RedisUserTokenRepository redisUserTokenRepository;

    public User getUser(Long userId) {
        return userRepository.findById(userId)
                .orElseThrow(() ->
                        new ResponseStatusException(HttpStatus.NOT_FOUND, "User not found"));
    }


    public void saveUserAccessToken(String accessCode, String refreshCode, Long userId) {

        // 받아온 code 저장
        String userTokenKey = "token" + userId;
        RedisUserToken userToken = RedisUserToken.builder()
                .userId(userTokenKey)
                .accessToken(accessCode)
                .refreshToken(refreshCode).build();

        redisUserTokenRepository.save(userToken);
    }

    public void updateUserAccessToken(Long userId) {
        // Token 갱신


    }

    public User getUserGoogleCalendarAndTask(RedisUserToken accessToken) {
        // 유저의 캘린더와 태스크 가져오기

        return null;
    }


}
