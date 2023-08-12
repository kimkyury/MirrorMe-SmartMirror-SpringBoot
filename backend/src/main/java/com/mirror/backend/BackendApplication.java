package com.mirror.backend;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.entity.VideoMessage;
import com.mirror.backend.api.repository.VideoRepository;
import com.mirror.backend.common.exception.FailConvertException;
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
import java.util.Optional;

@EnableScheduling
@SpringBootApplication
public class BackendApplication {

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @Autowired
    private VideoRepository videoRepository;

    public static void main(String[] args) {
        SpringApplication.run(BackendApplication.class, args);
    }

    @Scheduled(cron = "0 * * * * *")
    public void run() throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();

        LocalDateTime minusMinuteDate = LocalDateTime.now().minusMinutes(1);
        String dateMinusNow = minusMinuteDate.format(DateTimeFormatter.ofPattern("yyMMddHHmm"));

        String folderPath = "/message/" + dateMinusNow;

        File fileDirectory = Optional.of(new File(folderPath))
                .orElseThrow(() -> new FailConvertException("잘못된 파일입니다."));

        File[] files = fileDirectory.listFiles((dir, name) -> name.endsWith(".json"));
        if (files != null) {
            for (File file : files) {
                // redis 에 저장하는 로직 -> redis + mariaDB로 변경
                System.out.println("file = " + file);
                Message.RequestMessage videoMessage = objectMapper.readValue(file, Message.RequestMessage.class);

                String videoPath = folderPath + "/" + videoMessage.getFileName();
                VideoMessage vm = VideoMessage.builder()
                        .requestMessage(videoMessage)
                        .date(minusMinuteDate)
                        .build();

                Long videoId = videoRepository.save(vm).getVideoId();
                saveVideo(videoPath, videoId, vm);
            }
        }
    }
    public void saveVideo(String videoPath, Long videoId, VideoMessage videoMessage) {
        saveListToHash(videoMessage.getSendUserEmail(), videoId + "", videoPath);
    }

    public void saveListToHash(String hashKey, String innerKey, String innerValue) {
        HashOperations<String, String, String> hashOperations = redisTemplate.opsForHash();
        hashOperations.put(hashKey, innerKey, innerValue);
    }

}
