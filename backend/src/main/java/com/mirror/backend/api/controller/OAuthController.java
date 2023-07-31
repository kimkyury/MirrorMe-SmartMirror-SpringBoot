package com.mirror.backend.api.controller;

import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.service.OAuthService;
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


@RestController
@RequestMapping("/oauth")
@Tag(name = "OAuth", description = "OAuth 최초로그인 및 UserToken 관련 API")
public class OAuthController {

    @Autowired
    private OAuthService oAuthService;
    @Autowired
    private GoogleOAuth googleOAuth;

    static int SUCCESS = 1;
    static int FAIL = 0;

    @GetMapping
    @Operation(summary = "Google AuthorizationCode 발급 요청", description = "Google Login을 통해, Event와 Task의 접근권한이 부여된 Code를 요청합니다.")
    public ApiUtils.ApiResult<String> registerGoogle(HttpServletResponse response) throws Exception {

        String requestUrl = oAuthService.getRequestUrlForAuthorizationCode();
        response.sendRedirect(requestUrl.toString());

        return success("Success Request Authorization Code to Google");
    }

    @GetMapping("/google/callback")
    @Operation(summary = "Google Token 발급 요청", description = "Google에서 받은 Authorization Code를 Access/Refresh토큰으로 교환합니다")
    public ApiUtils.ApiResult<String> getUserToken(
            @RequestParam(name = "code", required = false) String authCode,
            @RequestParam(name = "error", required = false) String error
    ) throws IOException {

        if (error != null) {
            System.out.println("Can't run AuthorizationCode");
            return fail("Authorization Code 발급 문제");
        }
        // 승인코드 확인
        System.out.println("authCode: " + authCode);

        // 5. Access/Refresh Token으로 교환하기
        int result = oAuthService.getGoogleToken(authCode);
        if (result == FAIL) {
            System.out.println("Can't Get Access/Refresh");
            return fail("Access/Refresh Token 교환 문제");
        }

        // 6. userInfo 요청하기
        oAuthService.getUserEmail();

        // 7. 이미 존재하는 유저인지 확인한다


        // 존재하지 않는 유저라면, Redis에 회원 Token을 저장한다

        // 8. 로그인하라고 안내한다 (redirectUrl: home화면)


        return success("Access/Refresh Token 발급 성공");
    }

    @GetMapping("/dump")
    public ApiUtils.ApiResult<String> getUserToken(@RequestParam(name = "error", required = false) String error) {
//        System.out.println(error);
//        System.out.println("here is /oauth/token !");
//
//        String accessToken = String.valueOf(map.get("access_token"));
//        String expiresIn = String.valueOf(map.get("expires_in"));
//        String refreshToken = String.valueOf(map.get("refresh_token"));
//        String scope = String.valueOf(map.get("scope"));
//
//
//        Long userId = 1L; // 이 부분은 기존의 JSON에서 front가 userId를 붙여서 준다고 친다
//
//
//        System.out.println("json전체: " + map);
//        System.out.println("accessToken: " + accessToken);
//        System.out.println("expires_in: " + expiresIn);
//        System.out.println("refresh_token: " + refreshToken);
//        System.out.println("scope: " + scope);
//
//        oAuthService.saveUserAccessToken(accessToken, refreshToken, userId);
//
//        return success("로직 작성중");
        System.out.println("----------토큰 발급 성공----------");
        return success("로직 작성중");


    }


}
