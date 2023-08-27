package com.mirror.backend.api.service.impl;


import com.mirror.backend.api.dto.*;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.entity.keys.ConnectUserKey;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.api.service.SignUpService;
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
public class SignUpServiceImpl implements SignUpService {

    private final UserRepository userRepository;
    private final InterestRepository interestRepository;
    private final InterestCommonCodeRepository interestCommonCodeRepository;
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
            InterestKey interestId = new InterestKey(userId, interestCodes.get(i));
            InterestCommonCode interestCommonCode = interestCommonCodeRepository.findById(interestCodes.get(i)).orElse(null);

            Interest interest = Interest.builder()
                    .id(interestId)
                    .interestCode(interestCommonCode)
                    .user(user.get())
                    .isUsed(1)
                    .build();

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

        // TODO: 이미 해당 user가 household를 만든 적이 있다면 안 됨.

        Household newHousehold = Household.builder()
                .householdName(householdReq.getHouseholdName())
                .createUser(user)
                .build();
        householdRepository.save(newHousehold);

        // Household는 한 사람당 하나만 가능.
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

    public int registerHousehold(Long signUpUserId, Long householdId) {

        Optional<User> signUpUserOptional = userRepository.findByUserId(signUpUserId);
        Household household = householdRepository.findById(householdId).get();

        signUpUserOptional.ifPresent(selectUser -> {
            selectUser.setHousehold(household);
            userRepository.save(selectUser);
        });

        List<User> usersInSameHousehold = userRepository.findByHouseholdHouseholdId(householdId);

        if(usersInSameHousehold.size() != 0){

            for(User originalUser : usersInSameHousehold){

                if ( originalUser.equals(signUpUserOptional.get())) continue;

                // 가입자 기준
                ConnectUserKey connectUserOfSignUpUserKey = new ConnectUserKey(signUpUserId, originalUser.getUserId());
                ConnectUser connectUserOfSignUpUser = ConnectUser.builder()
                        .id(connectUserOfSignUpUserKey)
                        .user(signUpUserOptional.get())
                        .connectUser(originalUser)
                        .connectUserAlias(originalUser.getUserName())  // 해당 친인척의 실제이름을 기본값으로 함
                        .build();

                // 기존 사용자 기준
                ConnectUserKey connectUserKeyOfOriginalUserKey = new ConnectUserKey(originalUser.getUserId(), signUpUserId);
                ConnectUser connectUserOfOriginalUser = ConnectUser.builder()
                        .id(connectUserKeyOfOriginalUserKey)
                        .user(originalUser)
                        .connectUser(signUpUserOptional.get())
                        .connectUserAlias(signUpUserOptional.get().getUserName())  // 가입자의 실제이름을 기본값으로 함
                        .build();

                connectUserRepository.save(connectUserOfSignUpUser);
                connectUserRepository.save(connectUserOfOriginalUser);
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
