package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.RequestCreateUserDto;
import com.mirror.backend.api.dto.RequestHouseholdDto;
import com.mirror.backend.api.dto.ResponseHouseholdDto;
import com.mirror.backend.api.entity.Household;
import com.mirror.backend.api.entity.Interest;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.common.utils.Constants.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.time.LocalDateTime;
import java.util.Base64;
import java.util.List;
import java.util.Optional;

@Service
public class SignUpService {

    private final UserRepository userRepository;
    private final InterestRepository interestRepository;
    private final InterestCommonCodeRepository interestCommonCodeRepository;
    private final RedisTemplate<String, String> redisTemplate;
    private final HouseholdRepository householdRepository;
    private final MirrorRepository mirrorRepository;


    @Autowired
    public SignUpService(UserRepository userRepository,
                         InterestRepository interestRepository,
                         InterestCommonCodeRepository interestCommonCodeRepository, RedisTemplate<String, String> redisTemplate, HouseholdRepository householdRepository, MirrorRepository mirrorRepository) {
        this.userRepository = userRepository;
        this.interestRepository = interestRepository;
        this.interestCommonCodeRepository = interestCommonCodeRepository;
        this.redisTemplate = redisTemplate;
        this.householdRepository = householdRepository;
        this.mirrorRepository = mirrorRepository;
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


    // 프로필 이미지
    public int uploadProfileImage(String userEmail,  MultipartFile profileImg)  {
        try {
            byte[] bytes = profileImg.getBytes();
            String encodedImage = Base64.getEncoder().encodeToString(bytes);
            String key = "profileImg:" + userEmail;
            redisTemplate.opsForHash().put(key, "imageData", encodedImage);
        } catch (IOException e) {
            e.printStackTrace();
            return Result.REDIS_INSERT_ERROR;
        }

        return Result.SUCCESS;
    }

    public ResponseHouseholdDto createHousehold(Long userId, RequestHouseholdDto requestHouseholdDto) {

        Optional<User> userOptional = userRepository.findByUserId(userId);
        User user = userOptional.get();

        Household newHousehold = Household.builder()
                .householdName(requestHouseholdDto.getHouseholdName())
                .createUserId(userId)
                .build();

        householdRepository.save(newHousehold);

        Optional<Household> saveHousehold =householdRepository.findByCreateUserId(userId);

        ResponseHouseholdDto response = ResponseHouseholdDto.builder()
                .createUserName(user.getUserName())
                .createUserEmail(user.getUserEmail())
                .householdId(saveHousehold.get().getHouseholdId())
                .householdName(saveHousehold.get().getHouseholdName())
                .build();

        return response;
    }

    public ResponseHouseholdDto searchHousehold(String createUserEmail) {

        Optional<User> createUser = userRepository.findByUserEmail(createUserEmail);
        Optional<Household> targetHousehold = householdRepository.findByCreateUserId(createUser.get().getUserId());


        ResponseHouseholdDto response = ResponseHouseholdDto.builder()
                .createUserName(createUser.get().getUserName())
                .createUserEmail(createUser.get().getUserEmail())
                .householdId(targetHousehold.get().getHouseholdId())
                .householdName(targetHousehold.get().getHouseholdName())
                .build();

        return response;
    }
}
