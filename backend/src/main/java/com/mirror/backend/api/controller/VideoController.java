package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.service.VideoService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;


import java.util.List;
import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/video")
public class VideoController {

    @Autowired
    private VideoService videoService;

    @Value("${spring.servlet.multipart.location}")
    private String filePath;

    @PostMapping("/message")
    public ApiUtils.ApiResult<Integer> getMessageCheck(@RequestBody Message text) {
        return success(videoService.matchVideo(text.getText()));
    }

    @PostMapping
    public ApiUtils.ApiResult<Integer> postMessage(MultipartFile videoFile, MultipartFile voiceFile, @RequestPart("RequestMessage") Message.RequestMessage requestMessage) {
        String videoPath = videoService.transferFile(videoFile, filePath);
        String voicePath = videoService.transferFile(voiceFile, filePath);

        videoService.saveVideo(videoPath, voicePath, requestMessage);
        return success(1);
    }

    @GetMapping
    public ApiUtils.ApiResult<List<Message.ResponseMessage>> getMessage(@RequestParam int userId) {
        List<Message.ResponseMessage> video = videoService.getVideo(userId);
        return success(video);
    }
}
