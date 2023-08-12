package com.mirror.backend.api.service.impl;

import com.mirror.backend.api.dto.Message;
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
import org.springframework.web.multipart.MultipartFile;

import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
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
    public String getStringFromHash(String hashKey, String innerKey) {
        HashOperations<String, String, String> hashOperations = redisTemplate.opsForHash();
        return hashOperations.get(hashKey, innerKey);
    }

    // 영상 메시지 전체 조회
    @Override
    public List<VideoMessage> getVideo(String userEmail) {
        List<VideoMessage> videoMessageList = videoRepository.findAllByUserEmail(userEmail);
        return videoMessageList;
    }

    // 영상 메시지 한 개 조회
    @Override
    public FileInputStream getVideoDetail(Long videoId) throws FileNotFoundException {
        VideoMessage videoMessage = videoRepository.findByVideoId(videoId)
                .orElseThrow(() -> new NotFoundException("Not Found Video"));
        String videoUrl = getStringFromHash(videoMessage.getSendUserEmail(), videoId +"");
        return new FileInputStream(videoUrl);
    }

    @Override
    public List<Message.ResponseMessageCountFamily> getMessageCountFamily(Long userId, int month) {
        List<Message.ResponseMessageCountFamily> res = new ArrayList<>();
        List<ConnectUser> familyId = connectUserRepository.findByIdUserId(userId);
        for(ConnectUser connectUser : familyId) {
            Long connectUserId = connectUser.getId().getConnectUserId();

            String connectUserAlias = connectUser.getConnectUserAlias();
            String userEmail = userRepository.findByUserId(connectUserId).get().getUserEmail();

            Integer monthCount = videoRepository.findByMonth(month, userEmail);
            Message.ResponseMessageCountFamily responseMessageCountFamily = Message.ResponseMessageCountFamily.builder()
                    .connectUserAlias(connectUserAlias)
                    .messageCount(monthCount)
                    .build();
            res.add(responseMessageCountFamily);
        }
        return res;
    }

    @Override
    public String transferFile(MultipartFile videoFile, String filePath) {
        String originalFilename = videoFile.getOriginalFilename();
        String fileName = originalFilename.substring(originalFilename.lastIndexOf("\\") + 1);
        String uuid = UUID.randomUUID().toString();

        String saveFileName = filePath + File.separator + uuid + "_" + fileName;
        Path savePath = Paths.get(saveFileName);

        try {
            videoFile.transferTo(savePath);
            return saveFileName;
        }catch (IOException e) {
            e.printStackTrace();
        }

        return null;
    }
}
