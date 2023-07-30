package com.mirror.backend.api.controller;

import com.mirror.backend.api.info.GoogleOAuth;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.net.URLEncoder;

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
    @Operation(summary = "Google AuthorizationCode 발급 요청", description = "Google Login을 통해, Event와 Task의 접근권한이 부여된 Code를 요청합니다.")
    public ApiUtils.ApiResult<String> registerGoogle(HttpServletResponse response) throws Exception {

        String endPoint = googleOAuth.REQUEST_AUTH_CODE_URL;

        String redirectUri = googleOAuth.getRedirectUri();
        String clientId = googleOAuth.getClientId();
        String responseType = "code";
        String scopeCalendar = googleOAuth.SCOPE_CALENDAR;
        String scopeTask = googleOAuth.SCOPE_TASK;

        StringBuilder requestUrl = new StringBuilder();
        requestUrl.append(endPoint)
                .append("?client_id=").append(clientId)
                .append("&redirect_uri=").append(redirectUri)
                .append("&response_type=").append(responseType)
                .append("&scope=")
                .append(URLEncoder.encode(scopeCalendar + " ", "UTF-8"))
                .append(URLEncoder.encode(scopeTask + " ", "UTF-8"))
                .append("email");
//                .append("profile");

        System.out.println(requestUrl.toString());
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
            System.out.println("Not run AuthorizationCode");
            return fail("Authorization Code 문제로 인하여 실패");
        }

        // 승인코드 확인
        System.out.println("authCode: " + authCode);

        // 승인코드로 access, refresh 토큰으로 교환하기
        String endPoint = googleOAuth.REQUEST_TOKEN_URL;

        String clientId = googleOAuth.getClientId();
        String clientSecret = googleOAuth.getClientSecret();
        String code = authCode;
        String grantType = "authorization_code";
        String redirectUri = googleOAuth.getRedirectUri();

        RestTemplate restTemplate = new RestTemplate();

        MultiValueMap<String, String> map = new LinkedMultiValueMap<>();

        map.add("client_id", clientId);
        map.add("client_secret", clientSecret);
        map.add("code", code);
        map.add("grant_type", grantType);
        map.add("redirect_uri", redirectUri);

        System.out.println("!-----param 완성------!");
        System.out.println("endPoint: " + endPoint + "\n" + "responseEntity: " + map);


        ResponseEntity<String> responseEntity =
                restTemplate.postForEntity(endPoint, map, String.class);


        System.out.println("---------통과------------");
        System.out.println("endPoint: " + endPoint + "\n" + "responseEntity: " + responseEntity.toString());
        if (responseEntity.getStatusCode() == HttpStatus.OK) {
            return fail("Token 발급 실패");
        }

        // 6. userInfo 요청하기


        // 7. 이미 존재하는 유저인지 확인한다


        // 존재하지 않는 유저라면, Redis에 회원 Token을 저장한다

        // 8. 로그인하라고 안내한다 (redirectUrl: home화면)


        return success(responseEntity.toString());
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
