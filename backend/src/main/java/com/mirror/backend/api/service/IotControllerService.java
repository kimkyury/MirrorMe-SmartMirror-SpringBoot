package com.mirror.backend.api.service;


import org.springframework.stereotype.Service;

@Service
public class IotControllerService {


    public void fineUsersInfo(String mirrorId) {

        // DB에 없다면, 응답코드로 404를 날린다




        // DB에 존재한다면
        // 1. Mirror 테이블에서 해당 Mirrorid를 찾아온다
        // 2. {mirrorId}의 {mirror_group_id}를 찾아온다
        // 3. {mirror_group_id}를 가지고 users에서 user들을 찾아온다
        // 4. userList 각각에 대하여 userEmail을 통해 Redis내의 Profile을 가져온다
        // 5. encoding된 profile이미지를 Response에 담는다
        // 6. 해당값을 Json파일로 묶어서 내보낸다

    }


}
