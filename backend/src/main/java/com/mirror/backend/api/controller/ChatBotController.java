package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.TextDto.RequestChatBotDto;
import com.mirror.backend.api.dto.TextDto.ResponseChatBotDto;
import com.mirror.backend.api.dto.TextDto.TextSummaryScheduleDto;
import com.mirror.backend.api.service.ChatBotService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/chat")
public class ChatBotController {

    private final ChatBotService chatBotService;

    @Autowired
    public ChatBotController(ChatBotService chatBotService) {
        this.chatBotService = chatBotService;
    }

    // TODO: 없어질 메소드(Test 및 GPT 연결 확인용)
    @PostMapping("/question")
    public ApiUtils.ApiResult<ResponseChatBotDto> sendQuestion(@RequestBody RequestChatBotDto requestDto) {
        ResponseChatBotDto responseChatBotDto = chatBotService.askQuestion(requestDto);

        return success(responseChatBotDto);
    }

    @GetMapping("/calendar/summary")
    public ApiUtils.ApiResult<TextSummaryScheduleDto> getSummerySchedule(HttpServletRequest request){
        String userEmail = (String)request.getParameter("user_email");
        TextSummaryScheduleDto summaryScheduleDto = chatBotService.getSummerySchedule(userEmail);

        if ( summaryScheduleDto == null){
            return success(null);
        }
        return success(summaryScheduleDto);
    }
}
