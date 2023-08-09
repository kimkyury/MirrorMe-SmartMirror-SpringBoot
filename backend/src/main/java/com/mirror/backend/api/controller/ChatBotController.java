package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.chatbotDtos.RequestChatBotDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseChatBotDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseSummaryScheduleDto;
import com.mirror.backend.api.service.ChatBotService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

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
    public ApiUtils.ApiResult<ResponseChatBotDto> sendQuestion(@RequestBody RequestChatBotDto requestDto) {
        ResponseChatBotDto responseChatBotDto = chatBotService.askQuestion(requestDto);

        return success(responseChatBotDto);
    }

    @GetMapping("/calendar/summary")
    public ApiUtils.ApiResult<ResponseSummaryScheduleDto> getSummerySchedule(String userEmail){

        ResponseSummaryScheduleDto summaryScheduleDto = chatBotService.getSummerySchedule(userEmail);
        if ( summaryScheduleDto == null){
            return success(null);
        }
        return success(summaryScheduleDto);
    }
}
