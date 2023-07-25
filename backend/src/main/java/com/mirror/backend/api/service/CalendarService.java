package com.mirror.backend.api.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.dto.Event;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

@Service
public class CalendarService {

    private final String HTTP_REQUEST = "https://www.googleapis.com/calendar/v3/users/me/calendarList";
    private final String HTTP_REQUEST_PRE = "https://www.googleapis.com/calendar/v3/calendars/";
    private final String HTTP_REQUEST_POST = "/events";

    public String getCalendarList(String accessToken){
        try {
            String jsonData = "";

            URL url = new URL(HTTP_REQUEST + "?access_token=" + accessToken);

            BufferedReader bf = new BufferedReader(new InputStreamReader(url.openStream(), "UTF-8"));

            String line;
            while((line = bf.readLine()) != null){
                jsonData+=line;
            }
            return jsonData;
        } catch(Exception e) {
            return "error";
        }
    }

    public Event getMyCalendar(String accessToken, String calendarId) {
        try {
            String jsonData = "";

            URL url = new URL(HTTP_REQUEST_PRE + calendarId + HTTP_REQUEST_POST +  "?access_token=" + accessToken);

            BufferedReader bf = new BufferedReader(new InputStreamReader(url.openStream(), "UTF-8"));
            String line;
            while((line = bf.readLine()) != null){
                jsonData+=line;
            }

            System.out.println("jsonData = " + jsonData);
            ObjectMapper objectMapper = new ObjectMapper();
            Event event = objectMapper.readValue(jsonData, Event.class);
//            System.out.println("event.toString() = " + event.toString());
            return event;
        } catch(Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
