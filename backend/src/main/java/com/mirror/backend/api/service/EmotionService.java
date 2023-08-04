package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.entity.Emotion;

import java.util.List;

public interface EmotionService {
    Long saveEmotion(EmotionDto.EmotionReq emotionReq);
    List<EmotionDto.EmotionRes> getMyEmotion(Long userId);

}
