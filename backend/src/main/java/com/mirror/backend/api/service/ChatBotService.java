package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.chatbotDtos.RequestChatBotDto;
import com.mirror.backend.api.dto.chatbotDtos.RequestQuestionDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseChatBotDto;
import com.mirror.backend.api.info.ChatGPT;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class ChatBotService {
    private static RestTemplate restTemplate = new RestTemplate();
    private static ChatGPT chatGPT;

    @Autowired
    public ChatBotService(ChatGPT chatGPT) {
        this.chatGPT = chatGPT;
    }

    public HttpEntity<RequestChatBotDto> buildHttpEntity(RequestChatBotDto requestDto) {

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.parseMediaType(chatGPT.MEDIA_TYPE));
        headers.add(chatGPT.AUTHORIZATION, chatGPT.BEARER + chatGPT.API_KEY);
        return new HttpEntity<>(requestDto, headers);
    }

    public ResponseChatBotDto getResponse(HttpEntity<RequestChatBotDto> chatGptRequestDtoHttpEntity) {
        ResponseEntity<ResponseChatBotDto> responseEntity = restTemplate.postForEntity(
                chatGPT.URL,
                chatGptRequestDtoHttpEntity,
                ResponseChatBotDto.class);

        return responseEntity.getBody();
    }

    public ResponseChatBotDto askQuestion(RequestQuestionDto requestDto) {
        return this.getResponse(
                this.buildHttpEntity(
                        new RequestChatBotDto(
                                chatGPT.MODEL,
                                requestDto.getQuestion(),
                                chatGPT.MAX_TOKEN,
                                chatGPT.TEMPERATURE,
                                chatGPT.TOP_P
                        )
                )
        );
    }

}
