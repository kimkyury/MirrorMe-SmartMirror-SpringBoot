package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.RequestCreateUserDto;
import com.mirror.backend.api.dto.RequestHouseholdDto;
import com.mirror.backend.api.dto.RequestMirrorDto;
import com.mirror.backend.api.dto.ResponseHouseholdDto;
import com.mirror.backend.api.service.SignUpService;
import com.mirror.backend.common.utils.ApiUtils;
import com.mirror.backend.common.utils.Constants.Result;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;

import static com.mirror.backend.common.utils.ApiUtils.fail;
import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/signup")
@Tag(name = "signup", description = "최초 Google 로그인(회원가입)")
public class SignUpController {
    private SignUpService signUpService;

    @Autowired
    public SignUpController(SignUpService signUpService) {
        this.signUpService = signUpService;
    }

    @PostMapping("/profile")
    @Operation(summary = "Profile(userName, Interests) 생성", description = "가입 유저의 실제이름, 관심사 정보를 생성합니다. ")
    public ApiUtils.ApiResult<String> signUp(HttpServletRequest request,
                                             @RequestBody RequestCreateUserDto requestCreateUserDto) {

        String userEmail = (String) request.getAttribute("user_email");
        Long userId = (Long)request.getAttribute("user_id");

        // 해당 이메일을 가진 유저의 정보 업데이트하기
        int result = signUpService.updateInitUser(userEmail, userId,requestCreateUserDto);

        if ( result == Result.FAIL )
            return fail("user 추가 정보 생성 실패");
        return success("User 추가 정보 생성 성공");
    }

    @PostMapping("/profile/img")
    @Operation(summary = "Profile 이미지 등록", description = "프로필이미지를 등록합니다. ")
    public ApiUtils.ApiResult<String> updateProfileImage(HttpServletRequest request,
                                                         @RequestPart(value = "file") MultipartFile file) {

        String userEmail = (String) request.getAttribute("user_email");

        // 해당 이메일을 가진 유저의 정보 업데이트하기
        int result = signUpService.uploadProfileImage(userEmail, file);

        if ( result == Result.FAIL )
            return fail("user Profile Img 업데이트 실패");
        return success("User Profile Img 업데이트 성공");
    }

    // household 등록
    @PostMapping("/households")
    @Operation(summary = "새로운 가정 생성", description = "사용자가 새로운 가정을 생성합니다. ")
    public ApiUtils.ApiResult<ResponseHouseholdDto> createHousehold(HttpServletRequest request,
                                                                    @RequestBody RequestHouseholdDto requestHouseholdDto) {
        Long userId = (Long) request.getAttribute("user_id");

        ResponseHouseholdDto result = signUpService.createHousehold(userId, requestHouseholdDto);

        return success(result);
    }

    // household 조회
    @GetMapping("/households")
    @Operation(summary = "기존의 가정 검색", description = "사용자가 기존에 있는 가정을, 생성자 Email로 검색합니다. ")
    public ApiUtils.ApiResult<ResponseHouseholdDto> searchHousehold(HttpServletRequest request,
                                                        @RequestParam String createUserEmail) {

        String userEmail = (String) request.getAttribute("user_email");

        ResponseHouseholdDto result = signUpService.searchHousehold(createUserEmail );

        return success(result);
    }

    @PostMapping("/household")
    @Operation(summary = "사용자의 가정 등록", description = "사용자가 새로운 가정을 등록합니다. ")
    public ApiUtils.ApiResult<String> registerHousehold(HttpServletRequest request,
                                                        @RequestParam(name="householdId", required = true) Long householdId) {

        Long userId = (Long) request.getAttribute("user_id");

        int result = signUpService.registerHousehold(userId,householdId );


        return success("User Profile Img 업데이트 성공");
    }

    // Mirror 등록
    @PostMapping("/mirror")
    @Operation(summary = "사용자의 미러 등록", description = "사용자가 새로운 미러를 본인의 가정으로 등록합니다")
    public ApiUtils.ApiResult<String> registerMirror(HttpServletRequest request,
                                                        @RequestBody RequestMirrorDto requestMirrorDto) {

        String userEmail = (String) request.getAttribute("user_email");
        return success("User Profile Img 업데이트 성공");
    }

}
