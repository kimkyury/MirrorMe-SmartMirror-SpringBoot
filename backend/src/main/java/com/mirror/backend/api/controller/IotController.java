package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.IotRequestUserDto;
import com.mirror.backend.api.dto.IotResponseUserDto;
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
@Tag(name = "iot를 위한 APIs", description = "IOT전용")
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


        // DB에 존재한다면
        // 1. Mirror 테이블에서 해당 Mirrorid를 찾아온다
        // 2. {mirrorId}의 {mirror_group_id}를 찾아온다
        // 3. {mirror_group_id}를 가지고 users에서 user들을 찾아온다
        // 4. userList 각각에 대하여 userEmail을 통해 Redis내의 Profile을 가져온다
        // 5. encoding된 profile이미지를 Response에 담는다
        // 6. 해당값을 Json파일로 묶어서 내보낸다



        return success("usersInSameHousehold", users);

    }
}
