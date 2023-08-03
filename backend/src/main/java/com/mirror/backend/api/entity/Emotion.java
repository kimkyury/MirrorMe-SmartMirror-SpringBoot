package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Getter
@NoArgsConstructor
public class Emotion {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long emotionId;
    private int emotionCode;
    private LocalDate emotionDate;
    private Long userId;
    private LocalDateTime createAt;

    @Builder
    public Emotion(Long emotionId, int emotionCode, LocalDate emotionDate, Long userId, LocalDateTime createAt) {
        this.emotionId = emotionId;
        this.emotionCode = emotionCode;
        this.emotionDate = emotionDate;
        this.userId = userId;
        this.createAt = createAt;
    }
}
