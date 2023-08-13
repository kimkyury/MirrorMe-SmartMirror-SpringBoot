package com.mirror.backend.api.dto.TextDto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class TextVideoViewDto implements Serializable {

    private final String textCode = "0401";
    private String text;

    @Builder
    public TextVideoViewDto(String text) {
        this.text = text;
    }
}
