package com.mirror.backend.api.scheduler;


import com.mirror.backend.api.entity.RedisUserToken;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.Iterator;

@Component
public class SummaryCalendarService {

    RedisUserTokenRepository redisUserTokenRepository;

    @Autowired
    public SummaryCalendarService(RedisUserTokenRepository redisUserTokenRepository) {
        this.redisUserTokenRepository = redisUserTokenRepository;
    }

    // 1. Redis내의 유저 Token들을 모두 가져온다
    @Scheduled(cron = "5 * * * * ?")
    public void fetchRedisData() {
        System.out.println("------------실행중----------");
        // redis내의 유저 Token을 가져온다
        Iterable<RedisUserToken> redisUserTokenIterable= redisUserTokenRepository.findAll();
        Iterator<RedisUserToken> iterator = redisUserTokenIterable.iterator();

        while (iterator.hasNext()) {
            RedisUserToken token = iterator.next();
            // token 객체 처리
            System.out.println("token: " + token);
        }
    }
    // 2. 해당 UserToken으로 Calendar내역을 각각 가져온다

    // 3. 해당 Calendar내역을 3줄 요약하도록 GPT한테 요청한다




}
