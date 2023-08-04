package com.mirror.backend;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.entity.VideoMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.redis.core.HashOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;

import java.io.File;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

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
        ObjectMapper objectMapper = new ObjectMapper();

        LocalDateTime minusMinuteDate = LocalDateTime.now().minusMinutes(1);
        String dateMinusNow = minusMinuteDate.format(DateTimeFormatter.ofPattern("yyMMddHHmm"));

        System.out.println("dateNow = " + dateMinusNow);
        String folderPath = "/message/" + dateMinusNow;

        File fileDirectory = new File(folderPath);

        File[] files = fileDirectory.listFiles((dir, name) -> name.endsWith(".json"));
        if (files != null) {
            for (File file : files) {
                // redis 에 저장하는 로직
                System.out.println("file = " + file);
                VideoMessage videoMessage = objectMapper.readValue(file, VideoMessage.class);

                String videoPath = folderPath + "/" + videoMessage.getFileName();
                saveVideo(videoPath, videoMessage, dateMinusNow);
            }
        }
    }

    public void saveVideo(String videoPath, VideoMessage videoMessage, String date) {
        System.out.println("videoMessage = " + videoMessage.getUserEmail());
        saveListToHash(videoMessage.getSendUserEmail(), "sendUserEmail", videoMessage.getUserEmail());
        saveListToHash(videoMessage.getSendUserEmail(), "videoPath", videoPath);
        saveListToHash(videoMessage.getSendUserEmail(), "type", videoMessage.getType());
        saveListToHash(videoMessage.getSendUserEmail(), "date", date);
    }

    public void saveListToHash(String hashKey, String innerKey, String innerValue) {
        HashOperations<String, String, String> hashOperations = redisTemplate.opsForHash();
        String innerValuesStr = hashOperations.get(hashKey, innerKey);
        if(innerValuesStr == null) hashOperations.put(hashKey, innerKey, innerValue);
        else hashOperations.put(hashKey, innerKey, innerValuesStr + "," + innerValue);
    }
}
