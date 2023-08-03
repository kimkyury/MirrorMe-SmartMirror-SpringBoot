package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.entity.Emotion;
import com.mirror.backend.api.service.EmotionService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/emotion")
public class EmotionController {

    @Autowired
    private EmotionService emotionService;

    @PostMapping
    public ApiUtils.ApiResult<Long> postEmotion(@RequestBody EmotionDto.EmotionReq emotionReq) {
        return success(emotionService.saveEmotion(emotionReq));
    }

    @GetMapping
    public ApiUtils.ApiResult<List<Emotion>> getMyEmotion() {
        // 유저 가져오기
        return success(emotionService.getMyEmotion(1L));
    }
}
