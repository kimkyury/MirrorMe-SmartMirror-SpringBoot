package com.mirror.backend.api.dto;

import lombok.Builder;
import lombok.Getter;
import org.springframework.web.servlet.mvc.method.annotation.StreamingResponseBody;

@Getter
public class MessageDto {
    private String text;

    @Getter
    public static class RequestMessage {
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

        @Builder
        public ResponseMessageDetail(String userEmail, String sendUserEmail, String date, String type) {
            this.userEmail = userEmail;
            this.sendUserEmail = sendUserEmail;
            this.date = date;
            this.type = type;
        }
    }

    @Getter
    public static class ResponseMessageCountFamily {
        private String connectUserAlias;
        private int messageCount;

        @Builder
        public ResponseMessageCountFamily(String connectUserAlias, int messageCount) {
            this.connectUserAlias = connectUserAlias;
            this.messageCount = messageCount;
        }
    }

}
