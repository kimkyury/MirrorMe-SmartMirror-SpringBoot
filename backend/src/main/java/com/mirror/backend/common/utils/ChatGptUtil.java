package com.mirror.backend.common.utils;

import com.mirror.backend.api.info.ChatGPT;
import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatMessage;
import com.theokanning.openai.completion.chat.ChatMessageRole;
import com.theokanning.openai.service.OpenAiService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

@Component
@RequiredArgsConstructor
public class ChatGptUtil {

    public final ChatGPT chatGPT;
    private final OpenAiService openAiService;

    public String createMessage(String question){
        List<ChatMessage> messages = new ArrayList<>();

        // TODO: MessageRole의 USER와 SYSTEM의 차이를 모르겠음
        ChatMessage chatMessage = new ChatMessage(ChatMessageRole.SYSTEM.value(),
                question);
        messages.add(chatMessage);

        ChatCompletionRequest chatCompletionRequest = createChatCompletionRequest(messages);

        ChatMessage responseMessage = openAiService.createChatCompletion(chatCompletionRequest)
                .getChoices()
                .get(0)
                .getMessage();

        return responseMessage.getContent();
    }


    private ChatCompletionRequest createChatCompletionRequest(List<ChatMessage> messages){

        ChatCompletionRequest chatCompletionRequest = ChatCompletionRequest.builder()
                .model("gpt-3.5-turbo-0613")
                .messages(messages)
                .n(1)
                .maxTokens(300)
                .logitBias(new HashMap<>())
                .build();
        return chatCompletionRequest;
    }
}
