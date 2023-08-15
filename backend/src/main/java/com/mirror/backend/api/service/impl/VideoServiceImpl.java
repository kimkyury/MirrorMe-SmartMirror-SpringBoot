package com.mirror.backend.api.service.impl;

import com.mirror.backend.api.dto.MessageDto;
import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.entity.VideoMessage;
import com.mirror.backend.api.repository.ConnectUserRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.api.repository.VideoRepository;
import com.mirror.backend.api.service.VideoService;
import com.mirror.backend.common.exception.NotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.HashOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.io.*;
import java.util.*;

@Service
public class VideoServiceImpl implements VideoService {

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @Autowired
    private VideoRepository videoRepository;

    @Autowired
    private ConnectUserRepository connectUserRepository;

    @Autowired
    private UserRepository userRepository;

    @Override
    public int matchVideo(String text) {
        System.out.println("text = " + text);
        if(text.contains("영상") || text.contains("비디오")) {
            return 1;
        }
        return 0;
    }

    // 영상 메시지 전체 조회
    @Override
    public List<VideoMessage> getVideo(String userEmail) {
        List<VideoMessage> videoMessageList = videoRepository.findAllByUserEmail(userEmail);
        return videoMessageList;
    }

    // 영상 메시지 한 개 조회


    @Override
    public List<MessageDto.ResponseMessageCountFamily> getMessageCountFamily(Long userId, int month) {
        List<MessageDto.ResponseMessageCountFamily> res = new ArrayList<>();
        List<ConnectUser> familyId = connectUserRepository.findByIdUserId(userId);
        for(ConnectUser connectUser : familyId) {
            Long connectUserId = connectUser.getId().getConnectUserId();

            String connectUserAlias = connectUser.getConnectUserAlias();
            String userEmail = userRepository.findByUserId(connectUserId).get().getUserEmail();

            Integer monthCount = videoRepository.findByMonth(month, userEmail);
            MessageDto.ResponseMessageCountFamily responseMessageCountFamily = MessageDto.ResponseMessageCountFamily.builder()
                    .connectUserAlias(connectUserAlias)
                    .messageCount(monthCount)
                    .build();
            res.add(responseMessageCountFamily);
        }
        return res;
    }

    @Override
    public List<MessageDto.ResponseMessageDetail> unReadMessageList(String userEmail) {
        List<VideoMessage> videoMessageList = videoRepository.findAllByIsReadAndUserEmail('N', userEmail);

        List<MessageDto.ResponseMessageDetail> responseMessageDetailList = new ArrayList<>();
        for(VideoMessage videoMessage : videoMessageList) {
            MessageDto.ResponseMessageDetail responseMessageDto = MessageDto.ResponseMessageDetail.builder()
                    .userEmail(videoMessage.getUserEmail())
                    .sendUserEmail(videoMessage.getSendUserEmail())
                    .date(videoMessage.getDate().toString())
                    .type(videoMessage.getType())
                    .build();
            responseMessageDetailList.add(responseMessageDto);
        }
        return responseMessageDetailList;
    }

}
