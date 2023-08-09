package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.RequestCreateUserDto;
import com.mirror.backend.api.dto.RequestHouseholdDto;
import com.mirror.backend.api.dto.RequestMirrorDto;
import com.mirror.backend.api.dto.ResponseHouseholdDto;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.entity.keys.ConnectUserKey;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.common.utils.Constants.Result;
import com.mirror.backend.common.utils.IotEncryption;
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
    private final ConnectUserRepository connectUserRepository;
    private final IotEncryption iotEncryption;


    @Autowired
    public SignUpService(UserRepository userRepository,
                         InterestRepository interestRepository,
                         InterestCommonCodeRepository interestCommonCodeRepository, RedisTemplate<String, String> redisTemplate, HouseholdRepository householdRepository, MirrorRepository mirrorRepository, ConnectUserRepository connectUserRepository, IotEncryption iotEncryption) {
        this.userRepository = userRepository;
        this.interestRepository = interestRepository;
        this.interestCommonCodeRepository = interestCommonCodeRepository;
        this.redisTemplate = redisTemplate;
        this.householdRepository = householdRepository;
        this.mirrorRepository = mirrorRepository;
        this.connectUserRepository = connectUserRepository;
        this.iotEncryption = iotEncryption;
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

    public  ResponseHouseholdDto searchHousehold(String createUserEmail) {

        Optional<User> createUserOptional = userRepository.findByUserEmail(createUserEmail);
        if (createUserOptional.isEmpty()) return null;

        User createUser = createUserOptional.get();

        Optional<Household> targetHousehold = householdRepository.findByCreateUserId(createUser.getUserId());

        ResponseHouseholdDto response = ResponseHouseholdDto.builder()
                .createUserName(createUser.getUserName())
                .createUserEmail(createUser.getUserEmail())
                .householdId(targetHousehold.get().getHouseholdId())
                .householdName(targetHousehold.get().getHouseholdName())
                .build();

        return response;
    }

    public int registerHousehold(Long userId, Long householdId) {

        Optional<User> user = userRepository.findByUserId(userId);

        // 사용자에게 household 지정
        user.ifPresent(selectUser -> {
            selectUser.setHouseholdId(householdId);
            userRepository.save(selectUser);
        });

        // 해당 집에 이미 사람이 존재하는지 확인
        List<User> usersInSameHousehold = userRepository.findByHouseholdId(householdId);

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

    public int registerMirror(Long userId, RequestMirrorDto requestMirrorDto) {

        String mirrorId = requestMirrorDto.getMirrorId();
        String mirrorIdDecryption = iotEncryption.decryptionText(mirrorId);

        Long mirrorPlaceCode = requestMirrorDto.getMirrorPlaceCode();

        // 1. user의 householdId조희
        Optional<User> user = userRepository.findByUserId(userId);

        Mirror mirror = Mirror.builder()
                .mirrorId(mirrorIdDecryption)
                .mirrorGroupId(user.get().getHouseholdId())
                .mirrorPlaceCode(mirrorPlaceCode)
                .build();
        mirrorRepository.save(mirror);

        return Result.SUCCESS;

    }
}
