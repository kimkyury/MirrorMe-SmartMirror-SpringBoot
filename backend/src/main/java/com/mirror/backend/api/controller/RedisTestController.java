package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.RedisTest;
import com.mirror.backend.api.service.RedisTestService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/redistest")
@Tag(name="redistest", description = "레디스DB 테스트")
public class RedisTestController {

    @Autowired
    private RedisTestService redisTestService;

    @PostMapping
    @Operation(summary = "Redis DB 삽입 (userId, video) ")
    public int createRedisTest(@RequestParam("user_id") String userId, @RequestParam("vedio_url") String videoUrl) {

        int success = redisTestService.saveRedisTest(userId, videoUrl);

        // 음.. 생성이니까 실제개발시 성공여부만 출력하도록 수정하자
        System.out.println(success);
        return success;
    }

    @GetMapping
    @Operation(summary = "Redis DB 가져오기 (id) ")
    public ApiUtils.ApiResult<RedisTest> getAllRedisTest(@RequestParam("key") String key) {

        RedisTest redisTest  = redisTestService.getRedisTest(key);
        return success(redisTest);
    }

    @DeleteMapping("/{userId}")
    public int  deleteVideoUrl(@PathVariable String userId) {
        int success = redisTestService.deleteRedisTest(userId);
        return success;
    }





}