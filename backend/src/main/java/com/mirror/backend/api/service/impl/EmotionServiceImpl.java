package com.mirror.backend.api.service.impl;

import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.entity.Emotion;
import com.mirror.backend.api.repository.EmotionRepository;
import com.mirror.backend.api.service.EmotionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Service
public class EmotionServiceImpl implements EmotionService {

    @Autowired
    private EmotionRepository emotionRepository;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long saveEmotion(EmotionDto.EmotionReq emotionReq) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd");
        LocalDate date = LocalDate.parse(emotionReq.getEmotionDate(), formatter);

        Emotion emotion = Emotion.builder()
                .emotionCode(emotionReq.getEmotionCode())
                .emotionDate(date)
                .userId(emotionReq.getUserId())
                .createAt(LocalDateTime.now())
                .build();
        Emotion emotionEntity = emotionRepository.save(emotion);
        return emotionEntity.getEmotionId();
    }
}
