package com.mirror.backend.api.service.impl;

import com.mirror.backend.api.entity.VideoMessage;
import com.mirror.backend.api.repository.VideoRepository;
import org.apache.commons.io.IOUtils;
import org.apache.tomcat.util.codec.binary.Base64;
import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.service.VideoService;
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
    public Message.ResponseMessageDetail getVideoDetail(Long videoId) {
        VideoMessage videoMessage = videoRepository.findByVideoId(videoId);
        String videoUrl = getStringFromHash(videoMessage.getSendUserEmail(), videoId +"");

        try {
            InputStream inputStream = new FileInputStream(videoUrl);
            byte[] images = IOUtils.toByteArray(inputStream);
            byte[] byteEnc64 = Base64.encodeBase64(images);
            String imgStr = new String(byteEnc64, "UTF-8");

            videoMessage.update('Y');
            videoRepository.save(videoMessage);

            Message.ResponseMessageDetail responseMessage = Message.ResponseMessageDetail.builder()
                    .userEmail(videoMessage.getUserEmail())
                    .sendUserEmail(videoMessage.getSendUserEmail())
                    .date(videoMessage.getDate())
                    .type(videoMessage.getType())
                    .imgStr(imgStr)
                    .build();

            inputStream.close();
            return responseMessage;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
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
