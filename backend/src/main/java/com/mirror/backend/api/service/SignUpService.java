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

public interface SignUpService {

    public int updateInitUser(String userEmail, Long userId, UserDto.UserInitInfoReq userInitInfoReq );

    public int uploadProfileImage(String userEmail,  MultipartFile profileImg) ;

    public HouseholdDto.HouseholdPostRes createHousehold(Long userId, HouseholdDto.HouseholdReq householdReq);

    public HouseholdDto.HouseHoldGetRes searchHousehold(String createUserEmail);

    public int registerHousehold(Long signUpUserId, Long householdId);

    public int registerMirror(Long userId, MirrorDto.MirrorReq mirrorReq);
}
