package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.entity.Emotion;
import com.mirror.backend.api.service.EmotionService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

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
}
