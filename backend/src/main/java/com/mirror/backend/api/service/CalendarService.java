package com.mirror.backend.api.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.dto.Event;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

@Service
public class CalendarService {

    private final String HTTP_REQUEST_PRE = "https://www.googleapis.com/calendar/v3/calendars/";
    private final String HTTP_REQUEST_POST = "/events";


    public Event getMyCalendar(String accessToken, String calendarId) {
        try {
            String jsonData = "";

            URL url = new URL(HTTP_REQUEST_PRE + calendarId + HTTP_REQUEST_POST +  "?access_token=" + accessToken);

            BufferedReader bf = new BufferedReader(new InputStreamReader(url.openStream(), "UTF-8"));
            String line;
            while((line = bf.readLine()) != null){
                jsonData+=line;
            }

            ObjectMapper objectMapper = new ObjectMapper();
            Event event = objectMapper.readValue(jsonData, Event.class);
            return event;
        } catch(Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public List<Event.Item> getMyNowCalendar(Event event) {
        LocalDate now = LocalDate.now();
        List<Event.Item> items = new ArrayList<>();

        for( Event.Item item: event.getItems()) {

            String startTime = item.getStart().getDateTime();
            String endTime = item.getEnd().getDateTime();

            startTime = startTime == null ? item.getStart().getDate() : startTime.substring(0, 10);
            endTime = endTime == null ? item.getEnd().getDate() : endTime.substring(0, 10);
            DateTimeFormatter parser = DateTimeFormatter.ofPattern("yyyy-MM-dd");
            LocalDate localStartDate = LocalDate.parse(startTime, parser);
            LocalDate localEndDate = LocalDate.parse(endTime, parser);

            boolean chk = !now.isBefore(localStartDate) && !now.isAfter(localEndDate);
            if(chk) items.add(item);
        }

        return items;
    }
}
