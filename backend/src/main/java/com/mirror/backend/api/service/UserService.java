package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.RequestCreateUserDto;
import com.mirror.backend.api.entity.Interests;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.InterestsRepository;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.common.utils.Constants.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.server.ResponseStatusException;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private InterestsRepository interestsRepository;

    @Autowired
    private RedisUserTokenRepository redisUserTokenRepository;

    int SUCCESS = 1;
    int FAIL = 0;

    public User getUser(Long userId) {
        return userRepository.findById(userId)
                .orElseThrow(() ->
                        new ResponseStatusException(HttpStatus.NOT_FOUND, "User not found"));
    }

    public User createUser(String userEmail){
        User user = new User();
        user.setUserEmail(userEmail);
        return userRepository.save(user);
    }

    public int updateInitUser(String userEmail, RequestCreateUserDto requestCreateUserDto ){

        Optional<User> user = userRepository.findByUserEmail(userEmail);
        // userId찾기
        Long userId = user.get().getUserId();

        if ( user.isEmpty())
            return FAIL;

        String userName = requestCreateUserDto.getUserName();
        String userNickname = requestCreateUserDto.getUserNickname();
        List<Long> interestCodes = requestCreateUserDto.getInterestCodes();
        Long householdId = requestCreateUserDto.getHouseholdId();

        // 저장된 파일의 경로를 DB에 저장

        // uesrTable Update
        user.ifPresent(selectUser -> {
            selectUser.setUserName(userName);
            selectUser.setUserNickname(userNickname);
            selectUser.setHouseholdId(householdId);
            selectUser.setCreateAt(LocalDateTime.now());
            userRepository.save(selectUser);
        });

        // interests Create (multyKey1; userId, multiKey2: interestId)
        // 복합키 이용
        for(int i =0; i<interestCodes.size(); i++){
            InterestKey interestKey = new InterestKey();
            interestKey.setUserId(userId);
            interestKey.setInterestCode(interestCodes.get(i));

            Interests interest = new Interests();
            interest.setId(interestKey);
            interest.setIsUsed(1);

            interestsRepository.save(interest);
        }

        return SUCCESS;
    }



    public int uploadProfileImage(String userEmail, MultipartFile file) {
        Optional<User> user = userRepository.findByUserEmail(userEmail);

        String UPLOAD_DIR = "ImgTest/";  //TODO: 서버내의 절대경로로 바꿀 것

        Path filePath = null;

        try {

            Path resourceDirectory = Paths.get("src","main","resources", UPLOAD_DIR);
            String absolutePath = resourceDirectory.toFile().getAbsolutePath();

            filePath = Paths.get(absolutePath, file.getOriginalFilename());
            Files.write(filePath, file.getBytes());

        } catch (IOException e) {
            // 에러 처리
            e.printStackTrace();
        }

        System.out.println("이미지파일 저장경로: " + filePath.toString());
        Path finalFilePath = filePath;

        user.ifPresent(selectUser -> {
            selectUser.setProfileImageUrl(finalFilePath.toString());
            selectUser.setModifiedAt(LocalDateTime.now());
            userRepository.save(selectUser);
        });

        return Result.SUCCESS;
    }

    public boolean isExistUser(String email){

        Optional<User> user = userRepository.findByUserEmail(email);
        if(user.isEmpty()) return false;

        return true;
    }
}
