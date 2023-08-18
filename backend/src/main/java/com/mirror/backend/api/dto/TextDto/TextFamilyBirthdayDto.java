package com.mirror.backend.api.dto.TextDto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class TextFamilyBirthdayDto implements Serializable {

    private final String textCode = "0202";
    private String text;

    @Builder
    public TextFamilyBirthdayDto(String text) {
        this.text = text;
    }
}
