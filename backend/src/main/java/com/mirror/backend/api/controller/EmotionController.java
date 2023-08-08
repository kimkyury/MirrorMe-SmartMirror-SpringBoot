package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.entity.Emotion;
import com.mirror.backend.api.service.EmotionService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/emotion")
@Tag(name = "emotion", description = "감정 API")
public class EmotionController {

    @Autowired
    private EmotionService emotionService;

    @PostMapping
    @Operation(summary = "오늘 감정 저장", description = "iot와 통신하여 오늘의 감정을 저장합니다.")
    public ApiUtils.ApiResult<Long> postEmotion(@RequestBody EmotionDto.EmotionReq emotionReq) {
        return success(emotionService.saveEmotion(emotionReq));
    }

    @GetMapping
    @Operation(summary = "나의 감정 조회", description = "나의 일주일간의 감정을 조회합니다.")
    public ApiUtils.ApiResult<List<EmotionDto.EmotionRes>> getMyEmotion() {
        // 유저 가져오기
        return success(emotionService.getMyEmotion(1L));
    }
}
