package com.mirror.backend.api.dto.TextDto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class TextEmotionBasedContactRecommendationDto implements Serializable {

    private final String textCode = "0402";
    private String text;

    @Builder
    public TextEmotionBasedContactRecommendationDto(String text) {
        this.text = text;
    }
}
