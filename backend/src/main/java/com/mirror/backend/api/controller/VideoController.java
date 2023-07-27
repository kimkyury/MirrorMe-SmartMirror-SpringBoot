package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.service.VideoService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.UUID;

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
    public ApiUtils.ApiResult<Integer> postMessage(MultipartFile videoFile, MultipartFile voiceFile) {
        int userId = 1;
        String videoPath = videoService.transferFile(videoFile, filePath);
        String voicePath = videoService.transferFile(voiceFile, filePath);

        videoService.saveVideo(videoPath, voicePath);
        return success(1);
    }
}
