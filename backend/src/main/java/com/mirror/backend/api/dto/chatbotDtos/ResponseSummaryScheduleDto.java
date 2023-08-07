package com.mirror.backend.api.dto.chatbotDtos;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class ResponseSummaryScheduleDto implements Serializable {
    private String startText;
    private String summeryCalendarText;
    private String endText;

    @Builder
    public ResponseSummaryScheduleDto(String startText, String summeryCalendarText, String endText) {
        this.startText = startText;
        this.summeryCalendarText = summeryCalendarText;
        this.endText = endText;
    }
}
