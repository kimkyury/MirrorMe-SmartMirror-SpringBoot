package com.mirror.backend.api.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.dto.ResponseLoginDto;
import com.mirror.backend.api.dto.ResponseTokensDto;
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
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

import static com.mirror.backend.common.utils.ApiUtils.fail;
import static com.mirror.backend.common.utils.ApiUtils.success;


@RequestMapping()
@RestController
@Tag(name = "OAuth", description = "OAuth 최초로그인 및 UserToken 관련 API")
public class OAuthController {

    private OAuthService oAuthService;

    @Autowired
    public OAuthController(OAuthService oAuthService) {
        this.oAuthService = oAuthService;
    }

    @GetMapping("/oauth/login")
    @Operation(summary = "Google AuthorizationCode 발급 요청", description = "Google Login을 통해, Event와 Task의 접근권한이 부여된 Code를 요청합니다.")
    public void registerGoogleAccount(HttpServletResponse response) throws Exception {

        String requestUrl = oAuthService.getRequestUrlForAuthorizationCode();
        response.sendRedirect(requestUrl); //TODO: FrontUrl 로 변경

    }

    // 아래 메소드는 Front한테 위임되면서 삭제될 예정
    @GetMapping("/oauth/token")
    @Operation(summary = "(in Backend)Callback Token을 통한 로그인 진행", description = "" +
            "Google에서 받은 Authorization Code를 Access/Refresh토큰으로 교환, " +
            "이후 로그인을 진행합니다. \n ")
    public ApiUtils.ApiResult<ResponseLoginDto>  callback(
            @RequestParam(name = "code", required = false) String authCode,
            @RequestParam(name = "error", required = false) String error) {

        System.out.println("authCode: " + authCode);
        ResponseLoginDto response = oAuthService.login(authCode);

        Map<String, String> data = new HashMap<>();
        data.put("accessToken", response.getAccessToken());
        data.put("refreshToken", response.getAccessToken());

        String json = null;
        try {
            json = new ObjectMapper().writeValueAsString(data);
        }catch( JsonProcessingException e){
            e.printStackTrace();
        }
        String base64EncodedJson = Base64.getEncoder().encodeToString(json.getBytes(StandardCharsets.UTF_8));
        System.out.println(base64EncodedJson);
//        return "redirect:1ot://callback?token="  + base64EncodedJson;

        return success(response);
    }

    // 아래 메소드는 oauth/token으로 옮겨질 내용임 (Front연결이후)
    @GetMapping("/login/auth")
    @Operation(summary = "승인코드를 통한 유저 존재 확인 ",
            description = "Authorization Code를 Access/Refresh토큰으로 교환합니다." +
            "또한 유저 확인을 진행합니다.")
    public ApiUtils.ApiResult<ResponseLoginDto> confirmExistUser(
            @RequestParam(name = "code", required = false) String authCode) {

        ResponseLoginDto response = oAuthService.login(authCode);

        return success(response);
    }


    // TODO: 이 요청시에, 암호화를 넣어야할 것 같다.
    @GetMapping("/tokens")
    @Operation(summary= "(in Mirror) Refresh/Access Token 요청", description = "Mirror에서 특정 유저를 조회하기 위한 토큰입니다. ")
    public ApiUtils.ApiResult<ResponseTokensDto> getTokens(
            @RequestParam(name = "userEmail", required = false) String userEmail)  {

        userEmail = userEmail.replace("%40", "@");
        System.out.println("Email:" +userEmail);

        ResponseTokensDto tokenDto = oAuthService.getTokensFromUserEmail(userEmail);
        if ( tokenDto == null){
            return fail(null);
        }

        return success(tokenDto);
    }



}
