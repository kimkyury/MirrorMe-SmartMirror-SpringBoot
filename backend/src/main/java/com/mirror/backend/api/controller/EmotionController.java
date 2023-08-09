package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.entity.Emotion;
import com.mirror.backend.api.service.EmotionService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/emotion")
@Tag(name = "emotion", description = "감정 API")
public class EmotionController {

    @Autowired
    private EmotionService emotionService;

    @GetMapping
    @Operation(summary = "나의 감정 조회", description = "나의 일주일간의 감정을 조회합니다.")
    public ApiUtils.ApiResult<List<EmotionDto.EmotionRes>> getMyEmotion(HttpServletRequest request) {
        Long userId = (Long) request.getAttribute("user_id");
        userId = 2L;
        return success(emotionService.getMyEmotion(userId));
    }

    // 가족 감정 조회
    @GetMapping("/family")
    @Operation(summary = "가족 감정 조회", description = "가족의 일주일간의 감정을 조회합니다.")
    public ApiUtils.ApiResult<List<EmotionDto.EmotionFamilyResList>> getMyFamilyEmotion(HttpServletRequest request) {
        Long userId = (Long) request.getAttribute("user_id");
        userId = 2L;
        return success(emotionService.getFamilyEmotion(userId));
    }
}
