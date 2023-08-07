package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.entity.VideoMessage;
import com.mirror.backend.api.service.VideoService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;


import java.util.List;
import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/video")
public class VideoController {

    @Autowired
    private VideoService videoService;


    @PostMapping("/message")
    public ApiUtils.ApiResult<Integer> getMessageCheck(@RequestBody Message text) {
        return success(videoService.matchVideo(text.getText()));
    }

    @GetMapping
    public ApiUtils.ApiResult<List<VideoMessage>> getMessage(@RequestParam String userEmail) {
        List<VideoMessage> video = videoService.getVideo(userEmail);
        return success(video);
    }

    @GetMapping("/message")
    public ApiUtils.ApiResult<Message.ResponseMessageDetail> getOneMessage(@RequestParam Long videoId) {
        Message.ResponseMessageDetail video = videoService.getVideoDetail(videoId);
        return success(video);
    }

}
