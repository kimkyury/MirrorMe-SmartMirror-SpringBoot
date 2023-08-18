package com.mirror.backend.service;

import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.repository.ConnectUserRepository;
import com.mirror.backend.api.service.EmotionService;
import com.mirror.backend.api.service.impl.EmotionServiceImpl;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

//@SpringBootTest
public class EmotionServiceTest {

//    @Autowired
//    private EmotionServiceImpl emotionService;
//
//    @Autowired
//    private ConnectUserRepository connectUserRepository;
//
//    @Test
//    public void findAngryFamily() {
//        Long userId = 2L;
//
//        List<ConnectUser> familyId = connectUserRepository.findByIdUserId(userId);
//        System.out.println("familyId.toString() = " + familyId.toString());
//        List<User> userList = emotionService.familyAngryList(userId);
//
//        for (User user : userList) {
//            Long userIdFromList = user.getUserId();
//            if (userIdFromList.equals(5L) || userIdFromList.equals(10L)) {
//                assertEquals(userIdFromList, userId, "User ID is not as expected");
//            }
//        }
//    }
}
