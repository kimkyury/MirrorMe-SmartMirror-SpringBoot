package com.mirror.backend.api.controller;

import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.service.UserService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import static com.mirror.backend.common.utils.ApiUtils.success;


@RestController
@RequestMapping("/users")
@Tag(name="users", description = "유저 정보 API")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping
    @Operation(summary = "서버 정보 조회 테스트", description = "서버내의 MariaDB 접근을 테스트합니다" +
            "")
    public ApiUtils.ApiResult<User> getUser(@RequestParam("user_id") Long userId) {

        User exUser = userService.getUser(userId);
        System.out.println(exUser.toString());

        return success(exUser);
    }
}