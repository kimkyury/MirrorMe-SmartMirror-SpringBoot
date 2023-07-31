package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.ResponseLoginDto;
import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.UserService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

import static com.mirror.backend.common.utils.ApiUtils.fail;
import static com.mirror.backend.common.utils.ApiUtils.success;



@RequestMapping("/oauth")
@RestController
@Tag(name = "Oauth", description = "OAuth 최초로그인 및 UserToken 관련 API")
public class OAuthController {

    @Autowired
    private GoogleOAuth googleOAuth;
    @Autowired
    private OAuthService oAuthService;
    @Autowired
    private UserService userService;

    static int SUCCESS = 1;
    static int FAIL = 0;
    static int INIT_LOGIN_USER = 2;

    @GetMapping
    @Operation(summary = "Google AuthorizationCode 발급 요청", description = "Google Login을 통해, Event와 Task의 접근권한이 부여된 Code를 요청합니다.")
    public ApiUtils.ApiResult<String> registerGoogle(HttpServletResponse response) throws Exception {

        String requestUrl = oAuthService.getRequestUrlForAuthorizationCode();
        response.sendRedirect(requestUrl.toString());

        return success("Success Request Authorization Code to Google");
    }

    @GetMapping("/google/callback")
    @Operation(summary = "Callback Token을 통한 로그인 진행", description = "Google에서 받은 Authorization Code를 Access/Refresh토큰으로 교환, 이후 로그인을 진행합니다. \n 만약, isInitLoginUser값이 1이라면 최초 로그인 유저입니다.(회원가입, 추가정보 기입 필요)")
    public ApiUtils.ApiResult<ResponseLoginDto> userLogin(
            @RequestParam(name = "code", required = false) String authCode,
            @RequestParam(name = "error", required = false) String error
    ) throws IOException {
        ResponseLoginDto responseUserToken = null;

        System.out.println("authCode: " + authCode);

        if (error != null) {
            System.out.println("Can't run AuthorizationCode");
            return fail(null);
        }

        ResponseLoginDto response = oAuthService.login(authCode);
        System.out.println(response);
        System.out.println("Json 파일 준비완료" );
        return success(response);
    }

    @GetMapping("/")
    @Operation(summary = "Google AccessToken 재발급 요청", description = "AccessToken 만료로 인하여 RefreshToken을 통한 재발급 요청을 수행합니다. ")
    public ApiUtils.ApiResult<String> reissueToken(HttpServletResponse response) throws Exception {



        return success("Success Request Authorization Code to Google");
    }


}
