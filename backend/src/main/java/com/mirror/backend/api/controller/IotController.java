package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.dto.TextDto.*;
import com.mirror.backend.api.dto.UserDto;
import com.mirror.backend.api.service.EmotionService;
import com.mirror.backend.api.service.IotService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.core.io.Resource;
import org.springframework.util.FileCopyUtils;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.success;


@RequestMapping("/api/iot")
@RestController
@Tag(name = "iot", description = "IOT전용")
public class IotController {

    private IotService iotService;

    @Autowired
    private EmotionService emotionService;

    @Autowired
    IotController(IotService iotService){
        this.iotService = iotService;
    }

    @PostMapping("/users")
    @Operation(summary = "모든 유저 조회", description = "한 가정 내의 모든 유저 정보를 조회합니다.")
    public ApiUtils.ApiResult<List<UserDto.IotUsersRes>> getProfileImage(@RequestBody UserDto.IotUsersReq iotUsersReq) {

        String mirrorId = iotUsersReq.getMirrorId();
        List<UserDto.IotUsersRes> users = iotService.findUsersInfo(mirrorId);

        return success(users);
    }

    @GetMapping("/text/calendar/summary")
    @Operation(summary = "하루 일정 요약 TEXT 조회", description = "한 유저의 하루 일정 요약 TEXT를 조회합니다.")
    public ApiUtils.ApiResult<TextSummaryScheduleDto> getSummeryScheduleText(String userEmail){

        TextSummaryScheduleDto summaryScheduleTextDto = iotService.getSummerySchedule(userEmail);
        if ( summaryScheduleTextDto == null)
            return ApiUtils.success(null);

        return ApiUtils.success(summaryScheduleTextDto);
    }

    @GetMapping("/text/birth")
    @Operation(summary = "가족 생일 알림 TEXT 조회", description = "가족중 7일 이내에 생일인 사람과 선물 추천에 대한 TEXT를 조회합니다.")
    public ApiUtils.ApiResult<TextFamilyBirthdayDto> getBirthdayUserText(String userEmail){

        TextFamilyBirthdayDto textFamilyBirthdayDto = iotService.getBirthdayUserText(userEmail);
        if ( textFamilyBirthdayDto == null)
            return ApiUtils.success(null);

        return ApiUtils.success(textFamilyBirthdayDto);
    }

    @GetMapping("/text/video")
    @Operation(summary = "수신 메시지 안내 TEXT 조회", description = "수신된 메시지에 대한 TEXT를 조회합니다.")
    public ApiUtils.ApiResult<TextVideoViewDto> getVideoViewText(String userEmail){

        TextVideoViewDto textVideoViewDto = iotService.getTextVideoViewText(userEmail);
        if ( textVideoViewDto == null)
            return ApiUtils.success(null);

        return ApiUtils.success(textVideoViewDto);
    }

    @GetMapping("/text/contact")
    @Operation(summary = "가족 중 화난 사람에게 연락 권장 TEXT 조회", description = "가족 중 전날에 화가 나있던 사람에게 연락할 것을 권장하는 TEXT를 조회합니다. ")
    public ApiUtils.ApiResult<TextEmotionBasedContactRecommendationDto> getContactRecommendationText(String userEmail){

        TextEmotionBasedContactRecommendationDto textEmotionBasedContactRecommendationDto
                = iotService.getTextEmotionBasedContactRecommendationText(userEmail);
        if ( textEmotionBasedContactRecommendationDto == null)
            return ApiUtils.success(null);

        return ApiUtils.success(textEmotionBasedContactRecommendationDto);
    }

    @GetMapping("/text/rainy")
    @Operation(summary = "비 관련 TEXT조회", description = "비 유무에 따라 우산을 권장하는 TEXT를 조회합니다.")
    public ApiUtils.ApiResult<TextCautionRainyDto> getCautionRainyText(String userEmail){

        TextCautionRainyDto textCautionRainyDto = iotService.getCautionRainyText(userEmail);
        if ( textCautionRainyDto == null)
            return ApiUtils.success(null);

        return ApiUtils.success(textCautionRainyDto);
    }

    @GetMapping("/text/first")
    @Operation(summary = "유저 만남시 최초 TEXT 조회", description = "한 유저의 하루 중 최초 만남시의 TEXT를 조회합니다. (우선순위: Video > RecommendContact > Birth > Rainy > Calendar")
    public ApiUtils.ApiResult<TextFirstMeetingDto> getFirstMirrorText(String userEmail){

        TextFirstMeetingDto textFirstMeetingDto = iotService.getFirstMirrorTextDto(userEmail);
        if ( textFirstMeetingDto == null)
            return ApiUtils.success(null);

        return ApiUtils.success(textFirstMeetingDto);
    }

    @PostMapping
    @Operation(summary = "오늘 감정 저장", description = "iot와 통신하여 오늘의 감정을 저장합니다.")
    public ApiUtils.ApiResult<Long> postEmotion(@RequestBody @Valid EmotionDto.EmotionReq emotionReq) {
        return ApiUtils.success(emotionService.saveEmotion(emotionReq));
    }

    @GetMapping("/message")
    @Operation(summary = "회원 영상 조회", description = "영상 메시지 전체에서 얻은 videoId로 영상을 조회합니다. token이 필요합니다.")
    public Resource getOneMessage(@RequestParam Long videoId) throws IOException {
        FileInputStream videoDetail = iotService.getVideoDetail(videoId);
        return new ByteArrayResource(FileCopyUtils.copyToByteArray(videoDetail));
    }
}
