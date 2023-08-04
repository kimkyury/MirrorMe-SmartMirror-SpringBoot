package com.mirror.backend.api.entity;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "emotion_code")
public class EmotionCode {

    @Id
    private int emotionCode;
    private String emotionName;
}
