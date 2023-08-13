package com.mirror.backend.api.dto.chatbotDtos;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Getter
@NoArgsConstructor
public class ResponseFirstMirrorTextDto implements Serializable {

    private String textCode;
    private String textContent;

    @Builder
    public ResponseFirstMirrorTextDto(String textCode, String textContent) {
        this.textCode = textCode;
        this.textContent = textContent;
    }

    @Override
    public String toString() {
        return "ResponseFirstMirrorTextDto{" +
                "textCode='" + textCode + '\'' +
                ", textContent='" + textContent + '\'' +
                '}';
    }
}
