package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.RedisTest;
import com.mirror.backend.api.repository.RedisTestRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;


@Service
@RequiredArgsConstructor
public class RedisTestService {

    @Autowired
    private RedisTestRepository redisTestRepository;

    public int saveRedisTest(String userId, String videoUrl) {
        String key = "video" + userId;
        RedisTest send = new RedisTest(key, videoUrl);
        redisTestRepository.save(send);
        return 1;
    }

    public RedisTest getRedisTest(String userId) {
        String key = "video" + userId;

        Optional<RedisTest> receive = redisTestRepository.findById(key);
        RedisTest realR = receive.get();

        System.out.println(realR);
        return realR;
    }

    public int deleteRedisTest(String userId) {
        String key = "video" + userId;
        return 1;
    }
}
