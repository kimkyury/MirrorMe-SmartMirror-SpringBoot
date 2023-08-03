package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.RequestConnectUserInfoDto;
import com.mirror.backend.api.dto.RequestInterestDto;
import com.mirror.backend.api.dto.ResponseInterestDto;
import com.mirror.backend.api.dto.ResponseUserInfoDto;
import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.entity.Interest;
import com.mirror.backend.api.entity.InterestCommonCode;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.entity.keys.ConnectUserKey;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.ConnectUserRepository;
import com.mirror.backend.api.repository.InterestCommonCodeRepository;
import com.mirror.backend.api.repository.InterestRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.common.utils.Constants.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.util.*;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final InterestRepository interestRepository;
    private final InterestCommonCodeRepository interestCommonCodeRepository;
    private final ConnectUserRepository connectUserRepository;
    private RedisTemplate<String, String> redisTemplate;

    @Autowired
    public UserService(UserRepository userRepository, InterestRepository interestRepository,
                           InterestCommonCodeRepository interestCommonCodeRepository,
                       ConnectUserRepository connectUserRepository,
                        RedisTemplate<String, String> redisTemplate){
        this.userRepository = userRepository;
        this.interestRepository = interestRepository;
        this.interestCommonCodeRepository = interestCommonCodeRepository;
        this.connectUserRepository = connectUserRepository;
        this.redisTemplate = redisTemplate;
    }

    public User getUser(Long userId) {
        return userRepository.findById(userId)
                .orElseThrow(() ->
                        new ResponseStatusException(HttpStatus.NOT_FOUND, "User not found"));
    }

    public ResponseUserInfoDto getUserInfo(Long userId) {

        Optional<User> userOptional = userRepository.findByUserId(userId);

        User user = userOptional.get();
        ResponseUserInfoDto userInfo = ResponseUserInfoDto.builder()
                .userEmail(user.getUserEmail())
                .userName(user.getUserName())
                .createAt(user.getCreateAt())
                .modifiedAt(user.getModifiedAt())
                .householdId(user.getHouseholdId())
                .build();

        return userInfo;

    }

    public User createUser(String userEmail){
        User user = new User();
        user.setUserEmail(userEmail);
        return userRepository.save(user);
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

    public int createConnectUsersFromHouseholdId(Long userId, Long householdId) {

        // 1. householdId를 가지는 모든 회원들을 데려온다
        List<User> userInSameHouseholdList = userRepository.findByHouseholdId(householdId);

        if ( userInSameHouseholdList.size() == 0){
            return Result.NOT_FOUNT_USER;
        }

        // 2. 해당 회원들 각각의 Id와 userID를 이용하여 친인척 정보를 생성한다
        for(User targetUser : userInSameHouseholdList){
            ConnectUserKey connectUserKey = ConnectUserKey.builder()
                    .userId(userId)
                    .connectUserId(targetUser.getUserId())
                    .build();

            ConnectUser connectUser = ConnectUser.builder()
                    .id(connectUserKey)
                    .connectUserAlias(targetUser.getUserName())  // 해당 친인척의 실제이름을 기본값으로 함
                    .build();

            connectUserRepository.save(connectUser);
        }

        return Result.SUCCESS;
    }

    public List<ConnectUser> getConnectUsers(Long userId) {

        List<ConnectUser> connectUsers = connectUserRepository.findByIdUserId(userId);

        return connectUsers;
    }

    public int updateConnectUserAlias(Long userId, RequestConnectUserInfoDto dto) {

        Long connectUserId = dto.getConnectUserId();
        String connectUserAlias = dto.getConnectUserAlias(); //변경시키려는 이름

        // 1. 해당 userId와 connectUserAlias를 가진 사람이 없는지 확인한다 (별명의 중복방지를 위함..이었는데 그냥 중복허용시키자)
        // 왜냐면.. 친인척 추가시 디폴트값이 저장되면 어쩔 수 없이 중복될듯.
//        Optional<ConnectUser> connectUserOptional = connectUserRepository.findByIdUserIdAndConnectUserAlias(userId, connectUserAlias);
//
//        if (connectUserOptional.isPresent()){
//            return Result.FAIL;
//        }

        Optional<ConnectUser> updateConnectUserTargetOptional = connectUserRepository.findByIdUserIdAndIdConnectUserId(userId, connectUserId);

        updateConnectUserTargetOptional.ifPresent( selectConnectUser -> {
            selectConnectUser.setConnectUserAlias(connectUserAlias);
            connectUserRepository.save(selectConnectUser);
        });

        return Result.SUCCESS;
    }

}
