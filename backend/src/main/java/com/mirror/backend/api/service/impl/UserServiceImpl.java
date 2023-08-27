package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.*;
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
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.util.*;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final InterestRepository interestRepository;
    private final InterestCommonCodeRepository interestCommonCodeRepository;
    private final ConnectUserRepository connectUserRepository;
    private final RedisTemplate<String, String> redisTemplate;

    public UserDto.UserInfoRes getUserInfo(Long userId) {

        User user = userRepository.findByUserId(userId)
                .orElseThrow( () -> new NoSuchElementException());

        UserDto.UserInfoRes userInfo = UserDto.UserInfoRes.builder()
                .userEmail(user.getUserEmail())
                .userName(user.getUserName())
                .createAt(user.getCreateAt())
                .modifiedAt(user.getModifiedAt())
                .householdId(user.getHousehold().getHouseholdId())
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

        if ( user.isEmpty() )  return false;
        return true;
    }

    public List<InterestDto.InterestRes> getInterestDtoList(String userEmail, Long userId) {

        List<Interest> interests = interestRepository.findByIdUserIdAndIsUsed(userId, 1);
        List<InterestCommonCode> interestCodes = interestCommonCodeRepository.findAll();

        HashMap<Long, String> interestCodesMap = new HashMap<>();
        for( InterestCommonCode interestCode : interestCodes ){
            interestCodesMap.put(interestCode.getInterestCode(), interestCode.getInterestName());
        }

        List<InterestDto.InterestRes> responseInterestDtoList= new ArrayList<>();
        for(Interest interest : interests){
            Long interestCode = interest.getId().getInterestCode();
            String interestName = interestCodesMap.get(interestCode);
            InterestDto.InterestRes dto = new InterestDto.InterestRes(interestCode, interestName);
            responseInterestDtoList.add(dto);
        }

        return responseInterestDtoList;
    }

    public int updateInterest( Long userId, InterestDto.InterestReq interestReq) {

        int INTEREST_CREATED = 2;
        int INTEREST_OFF = 0;
        int INTEREST_ON = 1;

        Long interestCode = interestReq.getInterestCode();
        Optional<Interest> interestOptional = interestRepository.findByIdUserIdAndIdInterestCode(userId, interestCode);

        // 애초에 조회할 수 없는 애라면, userId와 code를 복합키로하여 생성한다
        if (interestOptional.isEmpty()){
            InterestKey interestKey = new InterestKey( userId, interestCode);
            InterestCommonCode interestCommonCode = interestCommonCodeRepository.findById(interestCode).get();

            Interest interest = Interest.builder()
                    .id(interestKey)
                    .interestCode(interestCommonCode)
                    .user(userRepository.findByUserId(userId).get())
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

        List<User> userInSameHouseholdList = userRepository.findByHouseholdHouseholdId(householdId);

        if ( userInSameHouseholdList.size() == 0){
            return Result.NOT_FOUNT_USER;
        }

        for(User targetUser : userInSameHouseholdList){
            ConnectUserKey connectUserKey = new ConnectUserKey(userId, targetUser.getUserId());

            ConnectUser connectUser = ConnectUser.builder()
                    .id(connectUserKey)
                    .connectUserAlias(targetUser.getUserName())
                    .build();

            connectUserRepository.save(connectUser);
        }

        return Result.SUCCESS;
    }

    public List<ConnectUserDto.ConnectUserRes> getConnectUsers(Long userId) {

        List<ConnectUser> connectUserList = connectUserRepository.findByIdUserId(userId);
        System.out.println(connectUserList);

        List<ConnectUserDto.ConnectUserRes> connectUserResList = new ArrayList<>();
        for(ConnectUser connectUser : connectUserList){
            ConnectUserDto.ConnectUserRes connectUserRes = ConnectUserDto.ConnectUserRes.builder()
                    .connectUserId(connectUser.getConnectUser().getUserId())
                    .connectUserName(connectUser.getConnectUser().getUserName())
                    .connectUserAlias(connectUser.getConnectUserAlias())
                    .build();

            connectUserResList.add(connectUserRes);
        }

        return connectUserResList;
    }

    public int updateConnectUserAlias(Long userId, ConnectUserDto.ConnectUserReq connectUserReq) {

        Long connectUserId = connectUserReq.getConnectUserId();
        String connectUserAlias = connectUserReq.getConnectUserAlias(); //변경시키려는 이름

        // TODO: 중복되는 별칭에 대한 처리 (But, 기본설정으로 실제이름이 들어가기에 중복은 발생할 수 밖에 없음)

        Optional<ConnectUser> connectUserOptional = connectUserRepository.findByIdUserIdAndIdConnectUserId(userId, connectUserId);
        connectUserOptional.ifPresent( selectConnectUser -> {
            selectConnectUser.setConnectUserAlias(connectUserAlias);
            connectUserRepository.save(selectConnectUser);
        });

        return Result.SUCCESS;
    }
}
