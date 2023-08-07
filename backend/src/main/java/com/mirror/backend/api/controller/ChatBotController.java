package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.chatbotDtos.RequestQuestionDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseChatBotDto;
import com.mirror.backend.api.service.ChatBotService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/chat")
public class ChatBotController {

    private final ChatBotService chatBotService;

    @Autowired
    public ChatBotController(ChatBotService chatBotService) {
        this.chatBotService = chatBotService;
    }

    @PostMapping("/question")
    public ApiUtils.ApiResult<ResponseChatBotDto> sendQuestion(@RequestBody RequestQuestionDto requestDto) {
        ResponseChatBotDto responseChatBotDto = chatBotService.askQuestion(requestDto);

        return success(responseChatBotDto);
    }
}
