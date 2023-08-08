package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/schedule")
@Tag(name="calendar", description = "사용자 캘린더 관련 API")
public class CalendarController {

    @Autowired
    private CalendarService calendarService;

    @GetMapping
    @Operation(summary = "회원 캘린더 전체 조회", description = "회원 login시 받는 code를 이용하여 회원의 전체 캘린더를 조회합니다." +
            "\n\n 만료된 AccessToken을 기입하면 RefreshToken이 요구되기 때문에 Error가 발생할 수 있습니다. " +
            "\n이 경우 개발자모드에서 Cookie로 RefreshToken을 담거나, PostMan으로 수행하세요. 참고로 난 그래서 만료AccessToken 테스트시 Postman으로만 테스트함\"")

    public ApiUtils.ApiResult<Event> getSchedule(HttpServletRequest request) {
        String accessToken = request.getHeader("access_token");

        Event resData = calendarService.getMyCalendar(accessToken, "primary");
        return success(resData);
    }

    @GetMapping("/today")
    @Operation(summary = "회원 캘린더 오늘 날짜 조회", description = "회원 login시 받는 token을 이용하여 회원의 오늘 날짜 캘린더 일정을 조회합니다.")
    public ApiUtils.ApiResult<List<Event.Item>> getScheduleNow(HttpServletRequest request) {
        String accessToken = request.getHeader("access_token");

        Event event = calendarService.getMyCalendar(accessToken, "primary");
        List<Event.Item> myNowCalendar = calendarService.getMyNowCalendar(event);
        return success(myNowCalendar);
    }

    @GetMapping("/today/count")
    @Operation(summary = "회원 캘린더 오늘 날짜 개수 조회", description = "회원 login시 받는 token을 이용하여 회원의 오늘 날짜 캘린더 일정의 개수를 조회합니다.")
    public ApiUtils.ApiResult<Integer> getScheduleNowCount(HttpServletRequest request) {
        String accessToken = request.getHeader("access_token");

        Event event = calendarService.getMyCalendar(accessToken, "primary");
        List<Event.Item> myNowCalendar = calendarService.getMyNowCalendar(event);
        return success(myNowCalendar.size());
    }
}


