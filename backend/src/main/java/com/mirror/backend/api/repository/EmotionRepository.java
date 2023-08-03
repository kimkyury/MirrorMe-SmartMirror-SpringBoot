package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.Emotion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EmotionRepository extends JpaRepository<Emotion, Long> {

}
