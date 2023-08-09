package com.mirror.backend.api.service.impl;

import com.mirror.backend.api.entity.VideoMessage;
import com.mirror.backend.api.repository.VideoRepository;
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
    public FileInputStream getVideoDetail(Long videoId) throws FileNotFoundException {
        VideoMessage videoMessage = videoRepository.findByVideoId(videoId);
        String videoUrl = getStringFromHash(videoMessage.getSendUserEmail(), videoId +"");

//        try {
//            InputStream inputStream =
//
//            StreamingResponseBody responseBody = outputStream -> {
//                byte[] buffer = new byte[1024];
//                int bytesRead;
//                while ((bytesRead = inputStream.read(buffer)) != -1) {
//                    outputStream.write(buffer, 0, bytesRead);
//                }
//                inputStream.close();
//            };
//
//            videoMessage.update('Y');
//            videoRepository.save(videoMessage);
//            return responseBody;
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
        return new FileInputStream(videoUrl);
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
