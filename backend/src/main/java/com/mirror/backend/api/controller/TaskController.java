package com.mirror.backend.api.controller;

import com.mirror.backend.api.dto.Task;
import com.mirror.backend.api.service.TaskService;
import com.mirror.backend.common.utils.ApiUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

import static com.mirror.backend.common.utils.ApiUtils.success;

@RestController
@RequestMapping("/tasks")
@Tag(name="task", description = "사용자 todoList 관련 API")
public class TaskController {

    @Autowired
    private TaskService taskService;

    @GetMapping()
    @Operation(summary = "회원 Task 전체 조회", description = "accessToken을 이용하여 회원의 전체 Task를 조회합니다.")
    public ApiUtils.ApiResult<List<Task>> getTask(@RequestParam("accessToken") String accessToken) {
        Task myTaskList = taskService.getMyTask(accessToken);

        List<Task> list = new ArrayList<>();
        for(Task.Item item : myTaskList.getItems()) {
            list.add(taskService.getMyTaskList(accessToken, item.getId()));
        }
        return success(list);
    }

}
