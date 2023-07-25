package com.mirror.backend.api.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.api.service.RestJsonService;
import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.json.JSONObject;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/schedule")
public class CalendarController {

    @Autowired
    private CalendarService calendarService;

    @Value("${calendar.client-id}")
    private String CLIENT_ID;

    @Value("${calendar.client-secret}")
    private String CLIENT_SECRET;

    @GetMapping
    public ApiUtils.ApiResult<String> getSchedule(@RequestParam("code") String code) throws JsonProcessingException {
        RestJsonService restJsonService = new RestJsonService();
        String accessTokenData = restJsonService.getAccessTokenJsonData(code, CLIENT_ID, CLIENT_SECRET);

        JSONObject accessTokenjsonObject = new JSONObject(accessTokenData);

        String accessToken = accessTokenjsonObject.get("access_token").toString();

        Event resData = calendarService.getMyCalendar(accessToken, "primary");
        System.out.println("User Json Data : " + resData);
        return success("success");
    }
}


