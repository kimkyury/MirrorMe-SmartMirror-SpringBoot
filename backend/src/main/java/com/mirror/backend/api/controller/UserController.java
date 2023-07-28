package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.CreateUserRequestDto;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.service.UserService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.net.URLEncoder;

import static com.mirror.backend.common.utils.ApiUtils.success;


@RestController
@RequestMapping("/users")
@Tag(name = "users", description = "유저 정보 API")
public class UserController {

    @Autowired
    private UserService userService;
    @Autowired
    private GoogleOAuth googleOAuth;


    @GetMapping("/oauth")
    public void registerGoogle(HttpServletResponse response) throws Exception {

        String endpoint = googleOAuth.getGoogleEndPoint();
        String redirectUri = googleOAuth.getGoogleRedirectUri();
        String client_id = googleOAuth.getGoogleClientId();
        String response_type = "code";

        String scopeGoogleCalendar = "https://www.googleapis.com/auth/calendar.events.readonly";
        String scopeGoogleTask = "https://www.googleapis.com/auth/tasks.readonly";

        String sendRedirectUrl = endpoint + "?" +
                "&redirect_uri=" + redirectUri +
                "&client_id=" + client_id +
                "&response_type=" + response_type +
                "&scope=" + URLEncoder.encode(scopeGoogleCalendar + " " + scopeGoogleTask, "UTF-8").replaceAll("\\+", "%20");

        System.out.println(sendRedirectUrl);

        response.sendRedirect(sendRedirectUrl);
    }

    @GetMapping("/oauth/code")
    public ApiUtils.ApiResult<Integer> getUserCode(@RequestParam String code) {

        System.out.print("code: " + code);
        return null;
    }


    @PostMapping("/signup")
    public ApiUtils.ApiResult<Integer> signUp(@RequestBody CreateUserRequestDto createUserRequestDto) {
        return null;

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
