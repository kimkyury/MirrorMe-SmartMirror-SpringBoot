package com.mirror.backend.api.dto.TextDto;

import lombok.*;

import javax.validation.constraints.NotNull;
import java.io.Serializable;


public class ChatBotDto{

    @Getter
    @Setter
    @ToString
    public static class ChatBotReq implements Serializable{

        @NotNull
        private String question;
    }

    @Getter
    @ToString
    public static class ChatBotRes implements Serializable{

        private String answer;

        @Builder
        public ChatBotRes(String answer) {
            this.answer = answer;
        }
    }



}
