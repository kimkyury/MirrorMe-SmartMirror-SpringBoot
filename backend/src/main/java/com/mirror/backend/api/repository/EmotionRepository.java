package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.Emotion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;

@Repository
public interface EmotionRepository extends JpaRepository<Emotion, Long> {
    List<Emotion> findAllByEmotionDateBetweenAndUserId(LocalDate start, LocalDate end, Long userId);
}
