package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.RequestCreateUserDto;
import com.mirror.backend.api.dto.RequestInterestDto;
import com.mirror.backend.api.dto.ResponseInterestDto;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.service.OAuthService;
import com.mirror.backend.api.service.UserService;
import com.mirror.backend.common.utils.ApiUtils;
import com.mirror.backend.common.utils.Constants.Result;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.fail;
import static com.mirror.backend.common.utils.ApiUtils.success;


@RestController
@RequestMapping("/users")
@Tag(name = "users", description = "유저 정보 API")
public class UserController {

    @Autowired
    private UserService userService;

    @Autowired
    private OAuthService oAuthService;

    @PostMapping("/signup")
    @Operation(summary = "OAuth 첫 로그인 이후, 부가 정보 작성", description = "실제이름, 닉네임, 가정id를 기입합니다. ")
    public ApiUtils.ApiResult<String> signUp(HttpServletRequest request,
                                             @RequestBody RequestCreateUserDto requestCreateUserDto) {

        String accessToken = request.getHeader("access_token");
        String userEmail = (String) request.getAttribute("user_email");
        Long userid = (Long)request.getAttribute("user_id");

        // 해당 이메일을 가진 유저의 정보 업데이트하기
        int result = userService.updateInitUser(userEmail, userid,requestCreateUserDto);

        if ( result == Result.FAIL )
            return fail("user 추가 정보 생성 실패");
        return success("User 추가 정보 생성 성공");
    }

    @PostMapping("/profile/img")
    @Operation(summary = "Profile 이미지 등록", description = "프로필이미지를 등록합니다. ")
    public ApiUtils.ApiResult<String> updateProfileImage(HttpServletRequest request,
                                             @RequestPart(value = "file") MultipartFile file) {

        String accessToken = request.getHeader("access_token");
        String userEmail = (String) request.getAttribute("user_email");

        // 해당 이메일을 가진 유저의 정보 업데이트하기
        int result = userService.uploadProfileImage(userEmail, file);

        if ( result == Result.FAIL )
            return fail("user Profile Img 업데이트 실패");

        return success("User Profile Img 업데이트 성공");
    }


    @GetMapping("/interests")
    public ApiUtils.ApiResult<List<ResponseInterestDto>> getMyInterests(HttpServletRequest request){

        // 이메일 찾기
        String userEmail = (String) request.getAttribute("user_email");
        Long userId = (Long) request.getAttribute("user_id");

        List<ResponseInterestDto> interestDtoList = userService.getInterestDtoList(userEmail, userId);

        if(interestDtoList.size() == 0)
            success("해당 User는 관심사가 없습니다");
        return success(interestDtoList);
    }

    @PostMapping("/interests")
    public ApiUtils.ApiResult<String> postMyInterest(HttpServletRequest request,
                                                     @RequestBody RequestInterestDto requestInterestDto){

        int INTEREST_CREATED = 2;
        int INTEREST_OFF = 0;
        int INTEREST_ON = 1;

        // 이메일 찾기
        String userEmail = (String) request.getAttribute("user_email");
        Long userId = (Long) request.getAttribute("user_id");
        int result  = userService.updateInterest(userEmail, userId, requestInterestDto);

        if (result == INTEREST_CREATED)
            return success("CREATE: Interest의 정보를 생성하였습니다. ");
        else if (result == INTEREST_OFF)
            return success("UPDATE: 해당 관심정보를 OFF하였습니다. (is_used = 0) ");
        else if (result == INTEREST_ON)
            return success("UPDATE: 해당 관심정보를 ON하였습니다. (is_used = 1)  ");

        return fail("수행불가");
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
