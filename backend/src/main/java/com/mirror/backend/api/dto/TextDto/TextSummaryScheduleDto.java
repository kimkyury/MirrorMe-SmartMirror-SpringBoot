package com.mirror.backend.api.dto.TextDto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class TextSummaryScheduleDto implements Serializable {

    private final String textCode = "0301";
    private String text;

    @Builder
    public TextSummaryScheduleDto(String text) {
        this.text = text;
    }
}
