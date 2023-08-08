package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.entity.VideoMessage;
import com.mirror.backend.api.service.VideoService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.method.annotation.StreamingResponseBody;


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

    @GetMapping(value = "/message", produces = MediaType.APPLICATION_OCTET_STREAM_VALUE)
    public ResponseEntity<StreamingResponseBody> getOneMessage(@RequestParam Long videoId) {
        StreamingResponseBody video = videoService.getVideoDetail(videoId);
        return ResponseEntity.ok()
                .contentType(MediaType.APPLICATION_OCTET_STREAM)
                .body(video);
    }

}
