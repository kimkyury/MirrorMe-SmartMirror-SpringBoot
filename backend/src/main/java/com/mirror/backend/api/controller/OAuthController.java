package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.*;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.common.utils.ApiUtils;
import com.mirror.backend.common.utils.Constants.Result;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;

import static com.mirror.backend.common.utils.ApiUtils.fail;
import static com.mirror.backend.common.utils.ApiUtils.success;


@RequestMapping("/oauth")
@RestController
@Tag(name = "OAuth", description = "OAuth 최초로그인 및 UserToken 관련 API")
public class OAuthController {

    private OAuthService oAuthService;

    @Autowired
    public OAuthController(OAuthService oAuthService) {
        this.oAuthService = oAuthService;
    }

    @GetMapping("/login")
    @Operation(summary = "Google AuthorizationCode 발급 요청", description = "Google Login을 통해, Event와 Task의 접근권한이 부여된 Code를 요청합니다.")
    public void registerGoogleAccount(HttpServletResponse response) throws Exception {

        String requestUrl = oAuthService.getRequestUrlForAuthorizationCode();
        response.sendRedirect(requestUrl);
    }
    @GetMapping("/auth")
    @Operation(summary = "(in Backend)Callback Token을 통한 로그인 진행", description = "" +
            "Google에서 받은 Authorization Code를 Access/Refresh토큰으로 교환, ")
    public void callback(
            @RequestParam(name = "code", required = false) String authCode,
            @RequestParam(name = "error", required = false) String error) {

        oAuthService.oAuthGoogleLogin(authCode);
    }

    @PostMapping("/login/password")
    @Operation(summary = "password 저장", description = "Google 로그인 유저의 비밀번호를 설정합니다. ")
    public ApiUtils.ApiResult<String> signUp(@Valid @RequestBody UserDto.UserSavePasswordReq userSavePasswordReq) {

        // 해당 이메일을 가진 유저의 정보 업데이트하기
        int result = oAuthService.saveUserPassword(userSavePasswordReq);

        if ( result == Result.FAIL )
            return fail("user Password 생성 실패");
        return success("User Password 생성 성공");
    }

    @PostMapping("/login/tokens")
    @Operation(summary= "Refresh/Access Token 요청", description = "로그인을 통해 유저확인 후 해당 유저의 Access/Refresh토큰을 반환합니다. ")
    public ApiUtils.ApiResult<LoginDto.LoginRes> signUp(@Valid @RequestBody LoginDto.LoginReq loginReq) {

        LoginDto.LoginRes loginRes = oAuthService.confirmLogin(loginReq);
        if ( loginRes == null)
            return fail(null);
        return success(loginRes);
    }


    // TODO: 이 요청시에, 암호화를 넣어야할 것 같다.
    @GetMapping("/tokens")
    @Operation(summary= "(in Mirror) Refresh/Access Token 요청", description = "Mirror에서 특정 유저를 조회하기 위한 토큰입니다. ")
    public ApiUtils.ApiResult<TokensDto.TokensRes> getTokens(
             @RequestParam(name = "userEmail") String userEmail)  {

        TokensDto.TokensRes tokenDto = oAuthService.getTokensFromUserEmail(userEmail);

        if ( tokenDto == null)
            return fail(null);
        return success(tokenDto);
    }
}
