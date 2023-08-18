package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.*;
import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.service.UserService;
import com.mirror.backend.common.utils.ApiUtils;
import com.mirror.backend.common.utils.Constants.Result;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.validation.Valid;
import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.fail;
import static com.mirror.backend.common.utils.ApiUtils.success;


@RestController
@RequestMapping("/user")
@Tag(name = "user", description = "유저 프로필 관련 API")
public class UserController {

    private UserService userService;

    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/profile")
    @Operation(summary = "본인 정보를 조회합니다(id제외).", description = "본인실명, 이메일, 생성/수정 시점, 가정ID를 조회합니다." )
    public ApiUtils.ApiResult<UserDto.UserInfoRes> getUserInfo(HttpServletRequest request) {

        Long userId = (Long) request.getAttribute("user_id");

        UserDto.UserInfoRes userInfoRes = userService.getUserInfo(userId);

        return success(userInfoRes);
    }

    @GetMapping("/profile/img")
    @Operation(summary = "Profile Image를 조회합니다", description = "프로필이미지의 encoding값을 조회합니다. ")
    public ResponseEntity<byte[]> getProfileImage(HttpServletRequest request) {

        String userEmail = (String)request.getAttribute("user_email");

        byte[] result = userService.getUserProfileImage(userEmail);

        HttpHeaders headers = new HttpHeaders();
        headers.setCacheControl("public, max-age=3600");  // Cache-Control 헤더를 설정하여 이미지를 캐싱할 수 있도록 함

        return ResponseEntity.ok()
                .headers(headers)
                .contentType(MediaType.IMAGE_JPEG)
                .body(result);
    }

    @GetMapping("/profile/interests")
    @Operation(summary = "관심사 정보를 조회합니다.", description = "어디에 관심있니" )
    public ApiUtils.ApiResult<List<InterestDto.InterestRes>> getMyInterests(HttpServletRequest request){

        // 이메일 찾기
        String userEmail = (String) request.getAttribute("user_email");
        Long userId = (Long) request.getAttribute("user_id");

        List<InterestDto.InterestRes> interestDtoList = userService.getInterestDtoList(userEmail, userId);

        if(interestDtoList.size() == 0)
            success("해당 User는 관심사가 없습니다");
        return success(interestDtoList);
    }

    @PostMapping("/interests")
    @Operation(summary = "관심사 정보를 생성/수정 합니다. ", description = "관심사 정보를 생성하거나, 기존에 이미 유저가 등록한 관심사라면 ON/OFF 합니다." )
    public ApiUtils.ApiResult<String> postMyInterest(HttpServletRequest request,
                                                     @Valid @RequestBody InterestDto.InterestReq interestReq){

        int INTEREST_OFF = 0;
        int INTEREST_ON = 1;
        int INTEREST_CREATED = 2;

        Long userId = (Long) request.getAttribute("user_id");
        int result  = userService.updateInterest( userId, interestReq);

        if (result == INTEREST_CREATED)
            return success("CREATE: Interest의 정보를 생성하였습니다. ");
        else if (result == INTEREST_OFF)
            return success("UPDATE: 해당 관심정보를 OFF하였습니다. (is_used = 0) ");
        else if (result == INTEREST_ON)
            return success("UPDATE: 해당 관심정보를 ON하였습니다. (is_used = 1)  ");

        return fail("수행불가");
    }

    @DeleteMapping
    @Operation(summary = "유저가 탈퇴합니다.", description = "탈퇴합니다. 관련된 연락처 정보나 관심사 정보도 함께 삭제되며, 단 Token정보는 삭제되지 않습니다." )
    public ApiUtils.ApiResult<String> deleteUser(HttpServletRequest request){

        Long userId = (Long)request.getAttribute("user_id");
        int result = userService.deleteUser(userId);

        if (result == Result.FAIL)
            fail("유저 탈퇴 실패했습니다.");

        return success("유저가 탈퇴되었습니다.");
    }

    @PostMapping("/friends")
    @Operation(summary = "특정 가정의 회원들을 추가합니다.",
            description = "mirror QR로 얻은 mirror_group_id를 통해 해당 가정 인원을 친구로 추가합니다." )
    public ApiUtils.ApiResult<String> getConnectUsers(HttpServletRequest request,
                                                                 @RequestParam(name = "householdId") Long householdId) {

        Long userId = (Long) request.getAttribute("user_id");
        int result = userService.createConnectUsersFromHouseholdId(userId, householdId);

        if ( result == Result.NOT_FOUNT_USER){
            return success("해당 가정에 등록된 사람이 없습니다." );
        }

        return success("추가 성공");
    }

    @GetMapping("/friends")
    @Operation(summary = "자신의 친인척 정보를 조회합니다.", description = "조회합니다." )
    public ApiUtils.ApiResult<List<ConnectUserDto.ConnectUserRes>> getConnectUsers(HttpServletRequest request) {

        Long userId = (Long) request.getAttribute("user_id");
        List<ConnectUserDto.ConnectUserRes> connectUsers = userService.getConnectUsers(userId);
        System.out.println(connectUsers);

        if ( connectUsers.size() == 0){
            success("해당 유저는 저장된 connectMember가 없습니다.");
        }
        return success(connectUsers);
    }

    @PutMapping("/friends")
    @Operation(summary = "자신의 친인척 별명을 수정합니다.", description = "수정하기" )
    public ApiUtils.ApiResult<String> updateConnectUserAlias(HttpServletRequest request,
                                                             @Valid @RequestBody ConnectUserDto.ConnectUserReq connectUserReq) {

        Long userId = (Long) request.getAttribute("user_id");
        int result = userService.updateConnectUserAlias(userId, connectUserReq);


        if ( result == Result.FAIL){
            return fail("해당 이름으로 저장된 지인정보가 존재합니다.");
        }
        return success("해당 지인의 별명이 수정되었습니다.");
    }


}
