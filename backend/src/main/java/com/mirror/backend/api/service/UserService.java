package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.*;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.common.utils.Constants.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.server.ResponseStatusException;

import java.io.IOException;
import java.time.LocalDateTime;
import java.util.*;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final InterestsRepository interestRepository;
    private final InterestCommonCodeRepository interestCommonCodeRepository;
    private final ConnectUserRepository connectUserRepository;
    private RedisTemplate<String, String> redisTemplate;

    @Autowired
    public UserService(UserRepository userRepository, InterestsRepository interestRepository,
                           InterestCommonCodeRepository interestCommonCodeRepository,
                       ConnectUserRepository connectUserRepository,
                        RedisTemplate<String, String> redisTemplate){
        this.userRepository = userRepository;
        this.interestRepository = interestRepository;
        this.interestCommonCodeRepository = interestCommonCodeRepository;
        this.connectUserRepository = connectUserRepository;
        this.redisTemplate = redisTemplate;
    }


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

    public int updateInitUser(String userEmail, Long userId, RequestCreateUserDto requestCreateUserDto ){

        Optional<User> user = userRepository.findByUserEmail(userEmail);
        // userId찾기

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

            Interest interest = new Interest();
            interest.setId(interestKey);
            interest.setIsUsed(1);

            interestRepository.save(interest);
        }
        return SUCCESS;
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
        }

        return Result.SUCCESS;
    }

    public byte[] getUserProfileImage(String userEmail) {
        String key = "profileImg:" + userEmail;
        String value = (String) redisTemplate.opsForHash().get(key, "imageData");

        byte[] imageData = Base64.getDecoder().decode(value);
        return imageData;
    }

    public boolean isExistUser(String email){

        Optional<User> user = userRepository.findByUserEmail(email);
        if(user.isEmpty()) return false;

        return true;
    }

    public List<ResponseInterestDto> getInterestDtoList(String userEmail, Long userId) {
        Optional<User> user = userRepository.findByUserEmail(userEmail);

        List<Interest> interests = interestRepository.findByIdUserIdAndIsUsed(userId, 1);
        List<InterestCommonCode> interestCodes = interestCommonCodeRepository.findAll();

        HashMap<Long, String> interestCodesMap = new HashMap<>();
        for( InterestCommonCode interestCode : interestCodes ){
            interestCodesMap.put(interestCode.getInterestCode(), interestCode.getInterestName());
        }

        List<ResponseInterestDto> responseInterestDtoList= new ArrayList<>();
        for(Interest interest : interests){
            Long interestCode = interest.getId().getInterestCode();
            String interestName = interestCodesMap.get(interestCode);
            ResponseInterestDto dto = new ResponseInterestDto(interestCode, interestName);
            responseInterestDtoList.add(dto);
        }
        return responseInterestDtoList;

    }

    public int updateInterest(String userEmail, Long userId, RequestInterestDto requestInterestDto) {

        int INTEREST_CREATED = 2;
        int INTEREST_OFF = 0;
        int INTEREST_ON = 1;


        Optional<User> user = userRepository.findByUserEmail(userEmail);

        Long interestCode = requestInterestDto.getInterestCode();
        Optional<Interest> interestOptional = interestRepository.findByIdUserIdAndIdInterestCode(userId, interestCode);

        // 애초에 조회할 수 없는 애라면, userId와 code를 복합키로하여 생성한다
        if (interestOptional.isEmpty()){
            InterestKey interestKey = new InterestKey( userId, interestCode);
            Interest interest = Interest.builder()
                    .id(interestKey)
                    .isUsed(1)
                    .build();
            interestRepository.save(interest);
            return INTEREST_CREATED;
        }

        // dto에 대하여, 이미 1이라면 0으로 만들고, 이미 0이라면 1로 만든다

        interestOptional.ifPresent(selectInterest -> {
            if ( selectInterest.getIsUsed() == INTEREST_OFF){
                selectInterest.setIsUsed(INTEREST_ON);
                interestRepository.save(selectInterest);
            }else{
                selectInterest.setIsUsed(INTEREST_OFF);
                interestRepository.save(selectInterest);
            }
        });



        return interestOptional.get().getIsUsed();
    }



    public int deleteUser(Long userId) {

        try {
            userRepository.deleteById(userId);
        } catch(Exception e){
            e.getMessage();
            return Result.FAIL;
        }
        return Result.SUCCESS;
    }


    public int updateUserNickname(Long userId, RequestUpdateUserNicknameDto dto) {

        Optional<User> user = userRepository.findByUserId(userId);

        user.ifPresent( selectUser -> {
           selectUser.setUserNickname(dto.getUserNickname());
           userRepository.save(selectUser);
        });

        return Result.SUCCESS;
    }

    public List<ConnectUser> getConnectUsers(Long userId) {

        List<ConnectUser> connectUsers = connectUserRepository.findByIdUserId(userId);

        return connectUsers;
    }

    public ResponseUserInfoDto getUserInfo(Long userId) {

        Optional<User> userOptional = userRepository.findByUserId(userId);

        User user = userOptional.get();
        ResponseUserInfoDto userInfo = ResponseUserInfoDto.builder()
                .userEmail(user.getUserEmail())
                .userNickname(user.getUserNickname())
                .userName(user.getUserName())
                .createAt(user.getCreateAt())
                .modifiedAt(user.getModifiedAt())
                .householdId(user.getHouseholdId())
                .profileImageUrl(user.getProfileImageUrl())
                .build();

        return userInfo;

    }


    public int updateConnectUserAlias(Long userId, RequestConnectUserInfoDto dto) {

        Long connectUserId = dto.getConnectUserId();
        String connectUserAlias = dto.getConnectUserAlias(); //변경시키려는 이름

        // 1. 해당 userId와 connectUserAlias를 가진 사람이 없는지 확인한다

        Optional<ConnectUser> connectUserOptional = connectUserRepository.findByIdUserIdAndConnectUserAlias(userId, connectUserAlias);

        if (connectUserOptional.isPresent()){
            return Result.FAIL;
        }

        Optional<ConnectUser> updateConnectUserTargetOptional = connectUserRepository.findByIdUserIdAndIdConnectUserId(userId, connectUserId);

        updateConnectUserTargetOptional.ifPresent( selectConnectUser -> {
            selectConnectUser.setConnectUserAlias(connectUserAlias);
            connectUserRepository.save(selectConnectUser);
        });

        return Result.SUCCESS;
    }
}
