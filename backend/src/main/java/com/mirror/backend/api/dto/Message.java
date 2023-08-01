package com.mirror.backend.api.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.web.multipart.MultipartFile;

@Getter
public class Message {
    private String text;

    @Getter
    @AllArgsConstructor
    public static class ResponseMessage {
        private String videoFile;
        private String voiceFile;
        private int userId;
        private int sendUserId;
    }

    @Getter
    @NoArgsConstructor
    @AllArgsConstructor
    public static class RequestMessage {
        private int userId;
        private int sendUserId;
    }
}
