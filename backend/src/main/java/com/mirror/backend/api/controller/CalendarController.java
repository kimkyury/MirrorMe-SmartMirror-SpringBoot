package com.mirror.backend.api.controller;

import com.mirror.backend.api.service.CalendarService;
import com.mirror.backend.api.service.RestJsonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.json.JSONObject;

@RestController
@RequestMapping("/schedule")
public class CalendarController {

    @Autowired
    private CalendarService calendarService;

    @GetMapping
    public String getSchedule(@RequestParam("code") String code) {
        RestJsonService restJsonService = new RestJsonService();
        String accessTokenData = restJsonService.getAccessTokenJsonData(code);

        JSONObject accessTokenjsonObject = new JSONObject(accessTokenData);

        String accessToken = accessTokenjsonObject.get("access_token").toString();
        System.out.println("accessToken = " + accessToken);

//        String calendarList = calendarService.getCalendarList(accessToken);
//        System.out.println("calendarList = " + calendarList);

        String userJsonData = calendarService.getMyCalendar(accessToken, "primary");
        if(userJsonData=="error") return "error";
        else System.out.println("User Json Data : " + userJsonData);
        return "success";
    }
}


