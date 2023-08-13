package com.mirror.backend.api.dto.chatbotDtos;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class ResponseFamilyBirthdayScheduleDto implements Serializable {
    private String familyBirthdayText;

    @Builder
    public ResponseFamilyBirthdayScheduleDto(String familyBirthdayText) {
        this.familyBirthdayText = familyBirthdayText;
    }
}
