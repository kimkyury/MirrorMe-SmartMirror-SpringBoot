package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.EmotionCount;
import com.mirror.backend.api.entity.keys.EmotionKey;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface EmotionCountRepository extends JpaRepository<EmotionCount, EmotionKey> {
    List<EmotionCount> findAllByEmotionKeyEmotionId(Long emotionId);
    Optional<EmotionCount> findByEmotionKeyEmotionIdAndEmotionKeyEmotionCode(Long emotionId, int emotionCode);
}
