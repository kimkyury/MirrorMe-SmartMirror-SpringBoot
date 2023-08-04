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
    public List<String> getListFromHash(String hashKey, String innerKey) {
        HashOperations<String, String, String> hashOperations = redisTemplate.opsForHash();
        String innerValuesStr = hashOperations.get(hashKey, innerKey);
        return List.of(innerValuesStr.split(","));
    }
    @Override
    public List<Message.ResponseMessage> getVideo(String userEmail) {
        List<String> sendIdList = getListFromHash(userEmail, "sendUserEmail");
        List<String> videoPathList = getListFromHash(userEmail, "videoPath");
        List<String> dateList = getListFromHash(userEmail, "date");

        if(sendIdList == null) {
            return null;
        }

        List<Message.ResponseMessage> responseMessages = new ArrayList<>();
        int size = sendIdList.size();
        System.out.println("size = " + size);
        for(int i = 0; i < size; i++) {
            String sendUserEmail = sendIdList.get(i);
            String videoPath = videoPathList.get(i);
            String date = dateList.get(i);

            try {
                InputStream inputStream = new FileInputStream(videoPath);
                byte[] images = IOUtils.toByteArray(inputStream);
                byte[] byteEnc64 = Base64.encodeBase64(images);
                String imgStr = new String(byteEnc64, "UTF-8");

                Message.ResponseMessage responseMessage = Message.ResponseMessage.builder()
                        .videoFile(imgStr)
                        .userEmail(userEmail)
                        .sendUserEmail(sendUserEmail)
                        .date(date).build();

                responseMessages.add(responseMessage);
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
