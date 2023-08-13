package com.mirror.backend.api.dto.chatbotDtos;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;


@Getter
@NoArgsConstructor
public class ResponseChatBotDto implements Serializable {

    private String result;

    @Builder
    public ResponseChatBotDto(String result) {
        this.result = result;
    }
}
