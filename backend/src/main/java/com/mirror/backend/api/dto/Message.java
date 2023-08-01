package com.mirror.backend.api.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import org.springframework.web.multipart.MultipartFile;

@Getter
public class Message {
    private String text;

    @Getter
    @AllArgsConstructor
    public static class ResponseMessage {
        private byte[] videoFile;
        private byte[] voiceFile;
        private int userId;
        private int sendUserId;
    }
}
