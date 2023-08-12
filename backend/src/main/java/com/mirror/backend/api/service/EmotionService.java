package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.dto.UserDto;
import com.mirror.backend.api.entity.Emotion;
import com.mirror.backend.api.entity.User;

import java.util.List;

public interface EmotionService {
    Long saveEmotion(EmotionDto.EmotionReq emotionReq);
    List<EmotionDto.EmotionRes> getMyEmotion(Long userId);
    List<EmotionDto.EmotionFamilyResList> getFamilyEmotion(Long userId);

    List<UserDto> familyAngryList(Long userId);
}
