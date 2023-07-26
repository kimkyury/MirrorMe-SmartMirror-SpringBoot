package com.mirror.backend.api.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.api.service.RestJsonService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.json.JSONObject;

import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/schedule")
@Tag(name="schedule", description = "사용자 캘린더 관련 API")
public class CalendarController {

    @Autowired
    private CalendarService calendarService;

    @Value("${calendar.client-id}")
    private String CLIENT_ID;

    @Value("${calendar.client-secret}")
    private String CLIENT_SECRET;

    @GetMapping
    @Operation(summary = "회원 캘린더 전체 조회", description = "회원 login시 받는 code를 이용하여 회원의 전체 캘린더를 조회합니다.")
    public ApiUtils.ApiResult<Event> getSchedule(@RequestParam("code") String code) {
        RestJsonService restJsonService = new RestJsonService();
        String accessTokenData = null;
        try {
            accessTokenData = restJsonService.getAccessTokenJsonData(code, CLIENT_ID, CLIENT_SECRET, 0);
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }

        JSONObject accessTokenjsonObject = new JSONObject(accessTokenData);

        String accessToken = accessTokenjsonObject.get("access_token").toString();
        System.out.println("accessToken = " + accessToken);
        // access_token을 받는다면 이 전 코드는 삭제
        Event resData = calendarService.getMyCalendar(accessToken, "primary");
        return success(resData);
    }

    @GetMapping("/today")
    @Operation(summary = "회원 캘린더 오늘 날짜 조회", description = "회원 login시 받는 code를 이용하여 회원의 오늘 날짜 캘린더 일정을 조회합니다.")
    public ApiUtils.ApiResult<List<Event.Item>> getScheduleNow(@RequestParam("accessToken") String accessToken) {
        Event event = calendarService.getMyCalendar(accessToken, "primary");
        List<Event.Item> myNowCalendar = calendarService.getMyNowCalendar(event);
        return success(myNowCalendar);
    }



}


