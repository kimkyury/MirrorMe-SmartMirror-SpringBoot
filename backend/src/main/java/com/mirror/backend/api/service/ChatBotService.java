package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.chatbotDtos.RequestChatBotDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseChatBotDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseSummaryScheduleDto;
import com.mirror.backend.api.entity.RedisSummeryCalendar;
import com.mirror.backend.api.info.ChatGPT;
import com.mirror.backend.api.repository.RedisSummeryCalendarRepository;
import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatMessage;
import com.theokanning.openai.completion.chat.ChatMessageRole;
import com.theokanning.openai.service.OpenAiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Optional;

@Service
public class ChatBotService {
    private final ChatGPT chatGPT;
    private final RedisSummeryCalendarRepository redisSummeryCalendarrepository;
    private OpenAiService openAiService;

    @Autowired
    public ChatBotService(ChatGPT chatGPT, RedisSummeryCalendarRepository redisSummeryCalendarrepository) {
        this.chatGPT = chatGPT;
        this.openAiService = chatGPT.openAiService();
        this.redisSummeryCalendarrepository = redisSummeryCalendarrepository;
    }

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

    public ResponseSummaryScheduleDto getSummerySchedule(String userEmail) {
        Optional<RedisSummeryCalendar> redisSummeryCalendar = redisSummeryCalendarrepository.findById(userEmail);

        if (redisSummeryCalendar.isEmpty()){
            return null;
        }

        ResponseSummaryScheduleDto dto = ResponseSummaryScheduleDto.builder()
                .summeryCalendarText(redisSummeryCalendar.get().getSummeryCalendar())
                .build();

        return dto;

    }
}
