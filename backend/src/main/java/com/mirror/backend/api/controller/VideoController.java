package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.MessageDto;
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

import javax.servlet.http.HttpServletRequest;
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
    @Operation(summary = "영상 메시지 확인 API", description = "iot측에서 주는 text로 영상메시지인지 조회합니다. token이 필요합니다.")
    public ApiUtils.ApiResult<Integer> getMessageCheck(@RequestBody MessageDto text, HttpServletRequest request) {
        return success(videoService.matchVideo(text.getText()));
    }

    @GetMapping
    @Operation(summary = "회원 영상 메시지 목록 전체 조회", description = "token에 담긴 userEmail로 영상 메시지를 조회합니다.")
    public ApiUtils.ApiResult<List<VideoMessage>> getMessage(HttpServletRequest request) {
        String userEmail = (String)request.getAttribute("user_email");
        List<VideoMessage> video = videoService.getVideo(userEmail);
        return success(video);
    }

    @GetMapping("/message")
    @Operation(summary = "회원 영상 조회", description = "영상 메시지 전체에서 얻은 videoId로 영상을 조회합니다. token이 필요합니다.")
    public Resource getOneMessage(@RequestParam Long videoId, HttpServletRequest request) throws IOException {
        FileInputStream videoDetail = videoService.getVideoDetail(videoId);
        return new ByteArrayResource(FileCopyUtils.copyToByteArray(videoDetail));
    }

    @GetMapping( "/message/count")
    @Operation(summary = "가족 영상 주고받은 개수 전체 조회", description = "마음의 온도(나와 가족들의 주고받은 횟수)를 조회합니다. token이 필요합니다.")
    public ApiUtils.ApiResult<List<MessageDto.ResponseMessageCountFamily>> getMessageCount(@RequestParam int month, HttpServletRequest request) throws IOException {
        Long userId = (Long) request.getAttribute("user_id");
        List<MessageDto.ResponseMessageCountFamily> messageCountFamily = videoService.getMessageCountFamily(userId, month);
        return success(messageCountFamily);
    }
}
