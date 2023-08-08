package com.mirror.backend.api.dto.chatbotDtos;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class RequestSummaryScheduleDto implements Serializable {
    private String startText;
    private String question;
    private String endText;

    @Builder
    public RequestSummaryScheduleDto(String startText, String question, String endText) {
        this.startText = startText;
        this.question = question;
        this.endText = endText;
    }
}
