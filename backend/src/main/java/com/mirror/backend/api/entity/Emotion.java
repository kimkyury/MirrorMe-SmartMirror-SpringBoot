package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Getter
@NoArgsConstructor
@Table(name = "emotion")
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
