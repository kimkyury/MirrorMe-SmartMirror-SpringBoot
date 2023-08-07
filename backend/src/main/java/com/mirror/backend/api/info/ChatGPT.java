package com.mirror.backend.api.info;

import com.theokanning.openai.service.OpenAiService;
import lombok.Getter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import java.time.Duration;

@Getter
@Component
public class ChatGPT {

    public static final String AUTHORIZATION = "Authorization";
    public static final String BEARER = "Bearer ";
    public static final String MODEL = "gpt-3.5-turbo-0613";
//    public static final String MODEL = "text-davinci-003";
    public static final Integer MAX_TOKEN = 1000;
    public static final Double TEMPERATURE = 0.0;
    public static final Double TOP_P = 1.0;
    public static final String MEDIA_TYPE = "application/json; charset=UTF-8";
//    public static final String URL = "https://api.openai.com/v1/completions";

    @Value("${chatgpt.api-key}")
    public String API_KEY;

    @Bean
    public OpenAiService openAiService(){
        return new OpenAiService(API_KEY, Duration.ofSeconds(60));
    }

}
