package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.TextDto.RequestChatBotDto;
import com.mirror.backend.api.dto.TextDto.ResponseChatBotDto;
import com.mirror.backend.api.dto.TextDto.TextSummaryScheduleDto;
import com.mirror.backend.api.entity.TextSummarySchedule;
import com.mirror.backend.api.info.ChatGPT;
import com.mirror.backend.api.repository.TextSummaryScheduleRepository;
import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatMessage;
import com.theokanning.openai.completion.chat.ChatMessageRole;
import com.theokanning.openai.service.OpenAiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class ChatBotService {
    private final ChatGPT chatGPT;
    private final TextSummaryScheduleRepository redisSummeryCalendarrepository;
    private OpenAiService openAiService;

    @Autowired
    public ChatBotService(ChatGPT chatGPT, TextSummaryScheduleRepository redisSummeryCalendarrepository) {
        this.chatGPT = chatGPT;
        this.openAiService = chatGPT.openAiService();
        this.redisSummeryCalendarrepository = redisSummeryCalendarrepository;
    }

    // TODO: 없어질 메소드(Test 및 GPT 연결 확인용)
    public ResponseChatBotDto askQuestion(RequestChatBotDto requestDto) {

        List<ChatMessage> messages = new ArrayList<>();
        ChatMessage systemMessage = new ChatMessage(ChatMessageRole.SYSTEM.value(),
                requestDto.getQuestion());
        messages.add(systemMessage);

        ChatCompletionRequest chatCompletionRequest = ChatCompletionRequest.builder()
                .model("gpt-3.5-turbo-0613")
                .messages(messages)
                .n(1)
                .maxTokens(300)
                .logitBias(new HashMap<>())
                .build();

        ChatMessage responseMessage = openAiService.createChatCompletion(
                chatCompletionRequest).getChoices().get(0).getMessage();
        messages.add(responseMessage);

        ResponseChatBotDto response = ResponseChatBotDto.builder()
                .result(responseMessage.getContent())
                .build();

        return response;
    }

    public TextSummaryScheduleDto getSummerySchedule(String userEmail) {
        TextSummarySchedule textSummarySchedule = redisSummeryCalendarrepository.findById(userEmail)
                .orElseThrow( () -> new NoSuchElementException());

        TextSummaryScheduleDto dto = TextSummaryScheduleDto.builder()
                .text(textSummarySchedule.getTextSummarySchedule())
                .build();

        return dto;
    }
}
