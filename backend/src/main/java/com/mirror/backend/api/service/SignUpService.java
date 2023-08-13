package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.*;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.entity.keys.ConnectUserKey;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.common.exception.NotFoundException;
import com.mirror.backend.common.utils.Constants.Result;
import com.mirror.backend.common.utils.IotEncryption;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.time.LocalDateTime;
import java.util.Base64;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class SignUpService {

    private final UserRepository userRepository;
    private final InterestRepository interestRepository;
    private final HouseholdRepository householdRepository;
    private final MirrorRepository mirrorRepository;
    private final ConnectUserRepository connectUserRepository;

    private final RedisTemplate<String, String> redisTemplate;
    private final IotEncryption iotEncryption;

    public int updateInitUser(String userEmail, Long userId, UserDto.UserInitInfoReq userInitInfoReq ){

        Optional<User> user = userRepository.findByUserEmail(userEmail);

        String userName = userInitInfoReq.getUserName();
        List<Long> interestCodes = userInitInfoReq.getInterestCodes();

        user.ifPresent(selectUser -> {
            selectUser.setUserName(userName);
            selectUser.setCreateAt(LocalDateTime.now());
            userRepository.save(selectUser);
        });

        // Save User's Init Interests
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

    public HouseholdDto.HouseholdPostRes createHousehold(Long userId, HouseholdDto.HouseholdReq householdReq) {

        User user = userRepository.findByUserId(userId).get();
        Household newHousehold = Household.builder()
                .householdName(householdReq.getHouseholdName())
                .createUser(user)
                .build();
        householdRepository.save(newHousehold);

        Household saveHousehold = householdRepository.findByCreateUserUserId(userId).get();
        HouseholdDto.HouseholdPostRes householdPostRes = HouseholdDto.HouseholdPostRes.builder()
                .createUserName(user.getUserName())
                .createUserEmail(user.getUserEmail())
                .householdId(saveHousehold.getHouseholdId())
                .householdName(saveHousehold.getHouseholdName())
                .build();

        return householdPostRes;
    }

    public HouseholdDto.HouseHoldGetRes searchHousehold(String createUserEmail) {

        User createUser = userRepository.findByUserEmail(createUserEmail).get();
        Optional<Household> household = householdRepository.findByCreateUserUserId(createUser.getUserId());
        if ( household.isEmpty()) return null;

        HouseholdDto.HouseHoldGetRes houseHoldGetRes = HouseholdDto.HouseHoldGetRes.builder()
                .createUserName(createUser.getUserName())
                .createUserEmail(createUser.getUserEmail())
                .householdId(household.get().getHouseholdId())
                .householdName(household.get().getHouseholdName())
                .build();

        return houseHoldGetRes;
    }

    public int registerHousehold(Long userId, Long householdId) {

        Optional<User> user = userRepository.findByUserId(userId);
        Household household = householdRepository.findById(householdId).get();

        // 사용자에게 household 지정
        user.ifPresent(selectUser -> {
            selectUser.setHousehold(household);
            userRepository.save(selectUser);
        });

        // 해당 집에 이미 사람이 존재하는지 확인
        List<User> usersInSameHousehold = userRepository.findByHouseholdHouseholdId(householdId);

        // 존재하는 사람들은 ConnectUser로 추가
        // 마찬가지로, 이미 존재했던 사람들도 해당 사람들이 뜨도록 쌍방으로 추
        if(usersInSameHousehold.size() != 0){

            for(User targetUser : usersInSameHousehold){

                // 가입자 기
                ConnectUserKey connectUserKey1 = ConnectUserKey.builder()
                        .userId(userId)
                        .connectUserId(targetUser.getUserId())
                        .build();

                ConnectUser connectUser = ConnectUser.builder()
                        .id(connectUserKey1)
                        .connectUserAlias(targetUser.getUserName())  // 해당 친인척의 실제이름을 기본값으로 함
                        .build();

                // 기존 사용자 기준
                ConnectUserKey connectUserKey2 = ConnectUserKey.builder()
                        .userId(targetUser.getUserId())
                        .connectUserId(userId)
                        .build();

                ConnectUser connectUser2 = ConnectUser.builder()
                        .id(connectUserKey2)
                        .connectUserAlias(user.get().getUserName())  // 가입자의 실제이름을 기본값으로
                        .build();

                connectUserRepository.save(connectUser);
                connectUserRepository.save(connectUser2);
            }
        }

        return Result.SUCCESS;
    }

    public int registerMirror(Long userId, MirrorDto.MirrorReq mirrorReq) {

        String mirrorId = mirrorReq.getMirrorId();
        String mirrorIdDecryption = iotEncryption.decryptionText(mirrorId);
        Long mirrorPlaceCode = mirrorReq.getMirrorPlaceCode();

        User user = userRepository.findByUserId(userId).orElseThrow(
                () -> new NotFoundException("해당 userId는 존재하지 않습니다. ")
        );

        Mirror mirror = Mirror.builder()
                .mirrorId(mirrorIdDecryption)
                .mirrorGroupId(user.getHousehold().getHouseholdId())
                .mirrorPlaceCode(mirrorPlaceCode)
                .build();
        mirrorRepository.save(mirror);

        return Result.SUCCESS;
    }
}
