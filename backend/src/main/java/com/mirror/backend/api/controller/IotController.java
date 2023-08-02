package com.mirror.backend.api.controller;


import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RequestMapping("/api/iot")
@RestController
@Tag(name = "iot를 위한 APIs", description = "IOT전용")
public class IotController {

    @GetMapping("/users")
    @Operation(summary = "Profile 이미지 조회", description = "프로필이미지 URL을 조회합니다. ")
    public ApiUtils.ApiResult<String> getProfileImage(HttpServletRequest request) {

        // Json으로 날라온 mirrorId가 DB에 존재하는지 확인한다

        // DB에 없다면, 응답코드로 404를 날린다

        // DB에 존재한다면
        // 1. Mirror 테이블에서 해당 Mirrorid를 찾아온다
        // 2. {mirrorId}의 {mirror_group_id}를 찾아온다
        // 3. {mirror_group_id}를 가지고 users에서 user들을 찾아온다
        // 4. userList 각각에 대하여 userEmail을 통해 Redis내의 Profile을 가져온다
        // 5. encoding된 profile이미지를 Response에 담는다
        // 6. 해당값을 Json파일로 묶어서 내보낸다



        return success("성공");

    }
}
