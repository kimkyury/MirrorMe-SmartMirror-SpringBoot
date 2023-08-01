package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.RequestCreateUserDto;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.UserService;
import com.mirror.backend.common.utils.ApiUtils;
import com.mirror.backend.common.utils.Constants.Result;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import static com.mirror.backend.common.utils.ApiUtils.fail;
import static com.mirror.backend.common.utils.ApiUtils.success;


@RestController
@RequestMapping("/users")
@Tag(name = "users", description = "유저 정보 API")
public class UserController {

    @Autowired
    private UserService userService;

    @Autowired
    private OAuthService oAuthService;

    @PostMapping("/signup")
    public ApiUtils.ApiResult<String> signUp(@RequestHeader("access_token") String accessToken,
                                             @RequestBody RequestCreateUserDto requestCreateUserDto) {
        // 이메일 찾기
        String userEmail = oAuthService.getUserEmailFromAccessToken(accessToken);
        // 해당 이메일을 가진 유저의 정보 업데이트하기
        int result = userService.updateInitUser(userEmail, requestCreateUserDto);

        if ( result == Result.FAIL ){
            return fail("user 추가 정보 생성 실패");
        }
        return success("User 추가 정보 생성 성공");
    }

    @PostMapping("/profile/img")
    public ApiUtils.ApiResult<String> updateProfileImage(@RequestHeader("access_token") String accessToken,
                                             @RequestPart(value = "file") MultipartFile file) {

        // 이메일 찾기
        String userEmail = oAuthService.getUserEmailFromAccessToken(accessToken);
        // 해당 이메일을 가진 유저의 정보 업데이트하기
        int result = userService.uploadProfileImage(userEmail, file);

        if ( result == Result.FAIL ){
            return fail("user Profile Img 업데이트 실패");
        }
        return success("User Profile Img 업데이트 성공");
    }


    @GetMapping
    @Operation(summary = "서버 정보 조회 테스트", description = "서버내의 MariaDB 접근을 테스트합니다" +
            "")

    public ApiUtils.ApiResult<User> getUser(@RequestParam("user_id") Long userId) {

        User exUser = userService.getUser(userId);
        System.out.println(exUser.toString());

        return success(exUser);
    }
}
