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

public interface UserService {

    public UserDto.UserInfoRes getUserInfo(Long userId);

    public User createUser(String userEmail);

    public byte[] getUserProfileImage(String userEmail);

    public boolean isExistUser(String email);

    public List<InterestDto.InterestRes> getInterestDtoList(String userEmail, Long userId) ;

    public List<ConnectUserDto.ConnectUserRes> getConnectUsers(Long userId);

    public int updateInterest( Long userId, InterestDto.InterestReq interestReq);

    public int deleteUser(Long userId);

    public int createConnectUsersFromHouseholdId(Long userId, Long householdId) ;

    public int updateConnectUserAlias(Long userId, ConnectUserDto.ConnectUserReq connectUserReq);
}
