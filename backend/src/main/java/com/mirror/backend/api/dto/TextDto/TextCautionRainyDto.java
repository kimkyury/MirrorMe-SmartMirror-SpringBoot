package com.mirror.backend.api.dto.TextDto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class TextCautionRainyDto implements Serializable {

    private final String textCode = "0301";
    private Long householdId;
    private String text;

    @Builder
    public TextCautionRainyDto(Long householdId, String text) {
        this.householdId = householdId;
        this.text = text;
    }
}
