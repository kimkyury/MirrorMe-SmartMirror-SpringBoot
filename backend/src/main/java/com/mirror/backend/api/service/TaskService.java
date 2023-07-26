package com.mirror.backend.api.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mirror.backend.api.dto.Event;
import com.mirror.backend.api.dto.Task;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

@Service
public class TaskService {
    private final String HTTP_REQUEST = "https://tasks.googleapis.com/tasks/v1/users/@me/lists";
    private final String HTTP_REQUEST_PRE = "https://tasks.googleapis.com/tasks/v1/lists/";
    public Task getMyTaskList(String accessToken, String TaskList) {
        try {
            String jsonData = "";

            URL url = new URL(HTTP_REQUEST_PRE + TaskList + "/tasks" +  "?access_token=" + accessToken);

            BufferedReader bf = new BufferedReader(new InputStreamReader(url.openStream(), "UTF-8"));
            String line;
            while((line = bf.readLine()) != null){
                jsonData+=line;
            }
            System.out.println("itemData = " + jsonData);
            ObjectMapper objectMapper = new ObjectMapper();
            Task task = objectMapper.readValue(jsonData, Task.class);
            return task;
        } catch(Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public Task getMyTask(String accessToken) {
        try {
            String jsonData = "";

            URL url = new URL(HTTP_REQUEST +  "?access_token=" + accessToken);

            BufferedReader bf = new BufferedReader(new InputStreamReader(url.openStream(), "UTF-8"));
            String line;
            while((line = bf.readLine()) != null){
                jsonData+=line;
            }
            System.out.println("jsonData = " + jsonData);
            ObjectMapper objectMapper = new ObjectMapper();
            Task task = objectMapper.readValue(jsonData, Task.class);
            return task;
        } catch(Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
