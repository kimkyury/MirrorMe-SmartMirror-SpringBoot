package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.IotRequestUserDto;
import com.mirror.backend.api.dto.IotResponseUserDto;
import com.mirror.backend.api.service.IotService;
import com.mirror.backend.common.utils.ApiResponse;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import static com.mirror.backend.common.utils.ApiResponse.success;


@RequestMapping("/api/iot")
@RestController
@Tag(name = "iot", description = "IOT전용")
public class IotController {

    private IotService iotService;

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
}
