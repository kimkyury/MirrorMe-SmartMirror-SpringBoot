package com.mirror.backend.api.dto.chatbotDtos;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class ResponseSummaryScheduleDto implements Serializable {
    private String summeryCalendarText;


    @Builder
    public ResponseSummaryScheduleDto(String summeryCalendarText) {
        this.summeryCalendarText = summeryCalendarText;
    }
}
