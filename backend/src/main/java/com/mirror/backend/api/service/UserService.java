package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.RequestCreateUserDto;
import com.mirror.backend.api.entity.Interests;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.InterestsRepository;
import com.mirror.backend.api.repository.RedisUserTokenRepository;
import com.mirror.backend.api.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

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

    public int updateInitUser(String userEmail, RequestCreateUserDto requestCreateUserDto ){

        Optional<User> user = userRepository.findByUserEmail(userEmail);

        if ( user.isEmpty()){
            return FAIL;
        }

        String userName = requestCreateUserDto.getUserName();
        String userNickname = requestCreateUserDto.getUserNickname();
        List<Long> interestCodes = requestCreateUserDto.getInterestCodes();

        Long userId = user.get().getUserId();

        user.ifPresent(selectUser -> {
            selectUser.setUserName(userName);
            selectUser.setUserNickname(userNickname);
            userRepository.save(selectUser);
        });

        // userId찾기


        // interests를 저장하도록 하기 (multyKey1; userId, multiKey2: interestId)
        // 복합키 생성
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

    public User createUser(String userEmail){
        User user = new User();
        user.setUserEmail(userEmail);

        return userRepository.save(user);
    }



    public boolean isExistUser(String email){

        Optional<User> user = userRepository.findByUserEmail(email);
        if(user.isEmpty()) return false;

        return true;
    }
}
