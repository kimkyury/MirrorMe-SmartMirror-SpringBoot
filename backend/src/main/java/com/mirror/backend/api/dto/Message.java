package com.mirror.backend.api.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.web.multipart.MultipartFile;

@Getter
public class Message {
    private String text;

    @Getter
    public static class ResponseMessage {
        private int idx;
        private String videoFile;
        private String userEmail;
        private String sendUserEmail;
        private String date;

        @Builder
        public ResponseMessage(int idx, String videoFile, String userEmail, String sendUserEmail, String date) {
            this.idx = idx;
            this.videoFile = videoFile;
            this.userEmail = userEmail;
            this.sendUserEmail = sendUserEmail;
            this.date = date;
        }
    }

}
