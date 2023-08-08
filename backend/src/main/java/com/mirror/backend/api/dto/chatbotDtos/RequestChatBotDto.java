package com.mirror.backend.api.dto.chatbotDtos;

import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class RequestChatBotDto implements Serializable {
    private String question;
}
