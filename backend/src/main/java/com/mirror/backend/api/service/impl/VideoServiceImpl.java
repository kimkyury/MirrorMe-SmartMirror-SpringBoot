package com.mirror.backend.api.service.impl;

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

    @Override
    public int matchVideo(String text) {
        System.out.println("text = " + text);
        if(text.contains("영상") || text.contains("비디오")) {
            return 1;
        }
        return 0;
    }

    @Override
    public void saveVideo(String videoPath, String voicePath, Message.RequestMessage requestMessage) {
        saveListToHash(requestMessage.getUserId()+"", "sendUserId", requestMessage.getSendUserId() + "");
        saveListToHash(requestMessage.getUserId()+"", "videoPath", videoPath);
        saveListToHash(requestMessage.getUserId()+"", "voicePath", voicePath);
    }

    public void saveListToHash(String hashKey, String innerKey, String innerValue) {
        HashOperations<String, String, String> hashOperations = redisTemplate.opsForHash();
        String innerValuesStr = hashOperations.get(hashKey, innerKey);
        hashOperations.put(hashKey, innerKey, innerValuesStr + "," + innerValue);
    }

    public List<String> getListFromHash(String hashKey, String innerKey) {
        HashOperations<String, String, String> hashOperations = redisTemplate.opsForHash();
        String innerValuesStr = hashOperations.get(hashKey, innerKey);
        return List.of(innerValuesStr.split(","));
    }
    @Override
    public List<Message.ResponseMessage> getVideo(int userId) {
        List<String> sendIdList = getListFromHash(userId + "", "sendUserId");
        List<String> videoPathList = getListFromHash(userId + "", "videoPath");
        List<String> voicePathList = getListFromHash(userId + "", "voicePath");

        if(sendIdList == null) {
            return null;
        }

        List<Message.ResponseMessage> responseMessages = new ArrayList<>();
        int size = sendIdList.size();
        for(int i = 0; i < size; i++) {
            String sendId = sendIdList.get(i);
            String videoPath = videoPathList.get(i);
            String voicePath = voicePathList.get(i);

            try {
                InputStream inputStream = new FileInputStream(videoPath);
                byte[] images = IOUtils.toByteArray(inputStream);
                byte[] byteEnc64 = Base64.encodeBase64(images);
                String imgStr = new String(byteEnc64, "UTF-8");

                inputStream = new FileInputStream(voicePath);
                images = IOUtils.toByteArray(inputStream);
                byteEnc64 = Base64.encodeBase64(images);
                String imgStr2 = new String(byteEnc64, "UTF-8");

                responseMessages.add(new Message.ResponseMessage(imgStr, imgStr2, userId, Integer.parseInt(sendId)));
                inputStream.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        return responseMessages;
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
