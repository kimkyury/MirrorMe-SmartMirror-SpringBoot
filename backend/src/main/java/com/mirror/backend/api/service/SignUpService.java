package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.RequestCreateUserDto;
import com.mirror.backend.api.entity.Interest;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.InterestCommonCodeRepository;
import com.mirror.backend.api.repository.InterestRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.common.utils.Constants.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
public class SignUpService {

    private final UserRepository userRepository;
    private final InterestRepository interestRepository;
    private final InterestCommonCodeRepository interestCommonCodeRepository;

    @Autowired
    public SignUpService(UserRepository userRepository,
                         InterestRepository interestRepository,
                         InterestCommonCodeRepository interestCommonCodeRepository) {
        this.userRepository = userRepository;
        this.interestRepository = interestRepository;
        this.interestCommonCodeRepository = interestCommonCodeRepository;
    }

    public int updateInitUser(String userEmail, Long userId, RequestCreateUserDto requestCreateUserDto ){

        Optional<User> user = userRepository.findByUserEmail(userEmail);
        if (user.isEmpty())
            return Result.NOT_FOUNT_USER;

        // Get dtoInfo
        String userName = requestCreateUserDto.getUserName();
        List<Long> interestCodes = requestCreateUserDto.getInterestCodes();

        // Update User (Nickame, UpdateTime)
        user.ifPresent(selectUser -> {
            selectUser.setUserName(userName);
            selectUser.setCreateAt(LocalDateTime.now());
            userRepository.save(selectUser);
        });

        // Create interests (multyKey1; userId, multiKey2: interestId)
        // 복합키 이용
        for(int i =0; i<interestCodes.size(); i++){
            InterestKey interestKey = new InterestKey();
            interestKey.setUserId(userId);
            interestKey.setInterestCode(interestCodes.get(i));

            Interest interest = new Interest();
            interest.setId(interestKey);
            interest.setIsUsed(1);

            interestRepository.save(interest);
        }
        return Result.SUCCESS;
    }


}
