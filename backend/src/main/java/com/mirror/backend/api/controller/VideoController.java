package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.entity.VideoMessage;
import com.mirror.backend.api.service.VideoService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.util.FileCopyUtils;
import org.springframework.web.bind.annotation.*;
import org.springframework.core.io.Resource;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.List;
import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/video")
@Tag(name = "video", description = "영상 메시지 API")
public class VideoController {

    @Autowired
    private VideoService videoService;

    @PostMapping("/message")
    @Operation(summary = "영상 메시지 확인 API", description = "iot측에서 주는 text로 영상메시지인지 조회합니다.")
    public ApiUtils.ApiResult<Integer> getMessageCheck(@RequestBody Message text) {
        return success(videoService.matchVideo(text.getText()));
    }

    @GetMapping
    @Operation(summary = "회원 영상 메시지 목록 전체 조회", description = "userEmail로 저장된 영상 목록을 보여줍니다.")
    public ApiUtils.ApiResult<List<VideoMessage>> getMessage(@RequestParam String userEmail) {
        List<VideoMessage> video = videoService.getVideo(userEmail);
        return success(video);
    }

    @GetMapping(value = "/message")
    public Resource getOneMessage(@RequestParam Long videoId) throws IOException {
        FileInputStream videoDetail = videoService.getVideoDetail(videoId);
        return new ByteArrayResource(FileCopyUtils.copyToByteArray(videoDetail));
    }

    @GetMapping(value = "/message")
    public ApiUtils.ApiResult<List<Message.ResponseMessageCountFamily>> getMessageCount(@RequestParam Long userId, @RequestParam int month) throws IOException {
        List<Message.ResponseMessageCountFamily> messageCountFamily = videoService.getMessageCountFamily(userId, month);
        return success(messageCountFamily);
    }

}
