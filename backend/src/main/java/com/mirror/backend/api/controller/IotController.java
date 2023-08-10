package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.dto.IotRequestUserDto;
import com.mirror.backend.api.dto.IotResponseUserDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseFirstMirrorTextDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseSummaryScheduleDto;
import com.mirror.backend.api.service.EmotionService;
import com.mirror.backend.api.service.IotService;
import com.mirror.backend.common.utils.ApiResponse;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import static com.mirror.backend.common.utils.ApiResponse.success;


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
    public ApiResponse<List<IotResponseUserDto>> getProfileImage(@RequestBody IotRequestUserDto iotRequestUsersDto) {

        // Json으로 날라온 mirrorId가 DB에 존재하는지 확인한다
        String mirrorId = iotRequestUsersDto.getMirrorId();
        System.out.println(mirrorId);

        // DB에 없다면, 응답코드로 404를 날린다
        boolean isExistMirror = iotService.findMirror(mirrorId);
        if (!isExistMirror)
            return ApiResponse.notFountMirror();

        List<IotResponseUserDto> users = iotService.fineUsersInfo(mirrorId);
        return success("usersInSameHousehold", users);
    }

    @GetMapping("/calendar/summary")
    public ApiUtils.ApiResult<ResponseSummaryScheduleDto> getSummerySchedule(String userEmail){

        ResponseSummaryScheduleDto summaryScheduleTextDto = iotService.getSummerySchedule(userEmail);
        if ( summaryScheduleTextDto == null){
            return ApiUtils.success(null);
        }
        return ApiUtils.success(summaryScheduleTextDto);
    }

    @GetMapping("/text/first")
    public ApiUtils.ApiResult<ResponseFirstMirrorTextDto> getFirstMirrorText(String userEmail){

        // TODO: 테스트용  output 고정 API
        ResponseFirstMirrorTextDto responseFirstMirrorTextDto =ResponseFirstMirrorTextDto.builder()
                .textCode("0101")
                .textContent("안녕하세요!, 오늘은 우산은 챙기시는 게 좋을 것 같아요")
                .build();

        if ( responseFirstMirrorTextDto == null){
            return ApiUtils.success(null);
        }
        return ApiUtils.success(responseFirstMirrorTextDto);
    }

    @PostMapping
    @Operation(summary = "오늘 감정 저장", description = "iot와 통신하여 오늘의 감정을 저장합니다.")
    public ApiUtils.ApiResult<Long> postEmotion(@RequestBody EmotionDto.EmotionReq emotionReq) {
        return ApiUtils.success(emotionService.saveEmotion(emotionReq));
    }
}
