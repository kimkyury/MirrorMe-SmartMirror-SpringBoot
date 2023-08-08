package com.mirror.backend.api.dto;

import com.mirror.backend.api.entity.VideoMessage;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.method.annotation.StreamingResponseBody;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Getter
public class Message {
    private String text;

    @Getter
    public static class  RequestMessage {
        private String userEmail;
        private String sendUserEmail;
        private String fileName;
        private String type;
    }

    @Getter
    public static class ResponseMessageDetail {
        private String userEmail;
        private String sendUserEmail;
        private String date;
        private String type;
        private StreamingResponseBody videoFile;

        @Builder
        public ResponseMessageDetail(String userEmail, String sendUserEmail, String date, String type, StreamingResponseBody videoFile) {
            this.userEmail = userEmail;
            this.sendUserEmail = sendUserEmail;
            this.date = date;
            this.type = type;
            this.videoFile = videoFile;
        }
    }
}
