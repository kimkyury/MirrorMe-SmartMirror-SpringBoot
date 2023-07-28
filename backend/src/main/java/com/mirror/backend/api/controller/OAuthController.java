package com.mirror.backend.api.controller;

import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.net.URLEncoder;
import java.util.HashMap;

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

    @GetMapping
    public ApiUtils.ApiResult<String> registerGoogle(HttpServletResponse response) throws Exception {

        String endpoint = googleOAuth.getGoogleEndPoint();
        String redirectUri = googleOAuth.getGoogleRedirectUriCode();
        String client_id = googleOAuth.getGoogleClientId();
        String response_type = "code";

        String scopeGoogleCalendar = "https://www.googleapis.com/auth/calendar.events.readonly";
        String scopeGoogleTask = "https://www.googleapis.com/auth/tasks.readonly";

        String sendRedirectUrl = endpoint + "?" +
                "&redirect_uri=" + redirectUri +
                "&client_id=" + client_id +
                "&response_type=" + response_type +
                "&scope=" + URLEncoder
                .encode(scopeGoogleCalendar + " " + scopeGoogleTask, "UTF-8")
                .replaceAll("\\+", "%20");

        return success("Oauth 로그인 페이지 전송 성공, Calendar, Task 요청 예정");
    }

    @GetMapping("/code")
    public ApiUtils.ApiResult<String> getUserToken(
            HttpServletResponse response,
            @RequestParam(name = "code", required = false) String code,
            @RequestParam(name = "error", required = false) String error
    ) throws IOException {

        if (error != null) {
            System.out.println("ApproveCode 발급 문제 발생");
            return fail("발급문제로 인하여 실패");
        }

        // 승인코드 확인
        System.out.println("code: " + code);

        // 승인코드로 access, refresh 토큰으로 교환하기
        String endPoint = googleOAuth.getGoogleEndPoint();
        String clientId = googleOAuth.getGoogleClientId();
        String clientSecret = googleOAuth.getGoogleClientSecret();
        String approveCode = code;
        String grantType = "authorization_code";
        String redirectUri = googleOAuth.getGoogleRedirectUriToken();

        StringBuilder requestUrl = new StringBuilder();
        requestUrl.append(endPoint)
                .append("&client_id" + clientId)
                .append("&client_secret" + clientSecret)
                .append("&approve_code" + approveCode)
                .append("&grant_type" + grantType)
                .append("&redirect_uri" + redirectUri);

        System.out.println(requestUrl.toString());
        response.sendRedirect(requestUrl.toString());

        return success("Call GetToken(Access, Refresh) 요청 중");
    }

    @ResponseBody
    @RequestMapping(value = "/token", method = RequestMethod.GET)
    public ApiUtils.ApiResult<String> getUserToken(
            @RequestBody HashMap<String, Object> map
    ) {

        String accessToken = String.valueOf(map.get("access_token"));
        String expiresIn = String.valueOf(map.get("expires_in"));
        String refreshToken = String.valueOf(map.get("refresh_token"));
        String scope = String.valueOf(map.get("scope"));
        Long userId = 1L; // 이 부분은 기존의 JSON에서 front가 userId를 붙여서 준다고 친다


        System.out.println("json전체: " + map);
        System.out.println("accessToken: " + accessToken);
        System.out.println("expires_in: " + expiresIn);
        System.out.println("refresh_token: " + refreshToken);
        System.out.println("scope: " + scope);

        oAuthService.saveUserAccessToken(accessToken, refreshToken, userId);

        return success("로직 작성중");
    }


}
