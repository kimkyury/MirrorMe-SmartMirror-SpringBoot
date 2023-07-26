package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.service.VideoService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/video")
public class VideoController {

    @Autowired
    private VideoService videoService;

    @PostMapping("/message")
    public ApiUtils.ApiResult<Integer> getMessage(@RequestBody Message text) {
        return success(videoService.matchVideo(text.getText()));
    } 


}
