package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.chatbotDtos.RequestQuestionDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseChatBotDto;
import com.mirror.backend.api.service.ChatBotService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/chat")
public class ChatBotController {

    private final ChatBotService chatBotService;

    @Autowired
    public ChatBotController(ChatBotService chatBotService) {
        this.chatBotService = chatBotService;
    }

    @PostMapping("/question")
    public ResponseChatBotDto sendQuestion(@RequestBody RequestQuestionDto requestDto) {
        return chatBotService.askQuestion(requestDto);
    }

}
