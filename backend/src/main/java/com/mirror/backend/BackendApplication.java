package com.mirror.backend;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.entity.VideoMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.redis.core.HashOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;
import java.util.UUID;

@EnableScheduling
@SpringBootApplication
public class BackendApplication {

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    public static void main(String[] args) {
        SpringApplication.run(BackendApplication.class, args);
    }

    @Scheduled(cron = "0 * * * * *")
    public void run() throws IOException {
        Date now = new Date();
        ObjectMapper objectMapper = new ObjectMapper();

        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyMMddHHmm");

        String imsi = "2308011033/";
        String folderPath = "/home/ubuntu/message/" + imsi;

        System.out.println("folderPath = " + folderPath);

        File fileDirectory = new File(folderPath);
        System.out.println("fileDirectory.listFiles() = " + fileDirectory.listFiles());
        System.out.println("fileDirectory.length() = " + fileDirectory.length());
        System.out.println("fileDirectory.isDirectory() = " + fileDirectory.isDirectory());

        File[] files = fileDirectory.listFiles((dir, name) -> name.endsWith(".json"));
        if (files != null) {
            System.out.println(" check ");
            for (File file : files) {
                System.out.println("Found JSON file: " + file.getAbsolutePath());

                // redis 에 저장하는 로직
                VideoMessage videoMessage = objectMapper.readValue(file, VideoMessage.class);

                String videoPath = folderPath + videoMessage.getFileName();
                System.out.println("videoPath = " + videoPath);
                saveVideo(videoPath, videoMessage);
            }
        }
        else {
            System.out.println("files = " + files);
        }
    }

    public void saveVideo(String videoPath, VideoMessage videoMessage) {
        saveListToHash(videoMessage.getUserId(), "sendUserId", videoMessage.getSendUserId());
        saveListToHash(videoMessage.getUserId(), "videoPath", videoPath);
        saveListToHash(videoMessage.getUserId(), "type", videoMessage.getType());
    }

    public void saveListToHash(String hashKey, String innerKey, String innerValue) {
        HashOperations<String, String, String> hashOperations = redisTemplate.opsForHash();
        String innerValuesStr = hashOperations.get(hashKey, innerKey);
        hashOperations.put(hashKey, innerKey, innerValuesStr + "," + innerValue);
    }
}
