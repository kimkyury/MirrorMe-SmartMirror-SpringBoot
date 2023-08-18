package com.mirror.backend.api.controller;


import com.mirror.backend.api.dto.*;
import com.mirror.backend.api.service.SignUpService;
import com.mirror.backend.common.utils.ApiUtils;
import com.mirror.backend.common.utils.Constants.Result;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import javax.validation.Valid;

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
                                             @Valid @RequestBody UserDto.UserInitInfoReq userInitInfoReq) {

        String userEmail = (String) request.getAttribute("user_email");
        Long userId = (Long)request.getAttribute("user_id");

        // 해당 이메일을 가진 유저의 정보 업데이트하기
        int result = signUpService.updateInitUser(userEmail, userId, userInitInfoReq);

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
    public ApiUtils.ApiResult<HouseholdDto.HouseholdPostRes> createHousehold(HttpServletRequest request,
                                                                           @Valid @RequestBody HouseholdDto.HouseholdReq householdReq) {
        Long userId = (Long) request.getAttribute("user_id");

        HouseholdDto.HouseholdPostRes householdPostRes = signUpService.createHousehold(userId, householdReq);

        return success(householdPostRes);
    }

    // household 조회
    @GetMapping("/households")
    @Operation(summary = "기존의 가정 검색", description = "사용자가 기존에 있는 가정을, 생성자 Email로 검색합니다. ")
    public ApiUtils.ApiResult<HouseholdDto.HouseHoldGetRes> searchHousehold(HttpServletRequest request,
                                                                             @RequestParam String createUserEmail) {

        HouseholdDto.HouseHoldGetRes result = signUpService.searchHousehold(createUserEmail);
        if ( result == null)
            success("해당 가정을 조회할 수 없습니다."); // 검색한 가정이 존재하지 않음

        return success(result);
    }

    @PostMapping("/household")
    @Operation(summary = "사용자의 가정 등록", description = "사용자가 새로운 가정을 등록하며, 자동으로 기존 사용자와의 관계를 업데이트합니다. ")
    public ApiUtils.ApiResult<String> registerHousehold(HttpServletRequest request,
                                                         @RequestParam(name="householdId") Long householdId) {

        Long userId = (Long) request.getAttribute("user_id");
        signUpService.registerHousehold(userId,householdId );

        return success("사용자 가정 등록 및, 기존 사용자간 연락처 업데이트 완료 ");
    }

    // Mirror 등록
    @PostMapping("/mirror")
    @Operation(summary = "사용자의 미러 등록", description = "사용자가 새로운 미러를 본인의 가정으로 등록합니다")
    public ApiUtils.ApiResult<String> registerMirror(HttpServletRequest request,
                                                      @RequestBody MirrorDto.MirrorReq mirrorReq) {

        Long userId = (Long) request.getAttribute("user_id");

        // TODO: mirrorId가 암호화 되어있다면 암호화 로직을 포함시켜야 함
        int result = signUpService.registerMirror(userId, mirrorReq);

        return success("Mirror 등록 완료");
    }

}
