package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.Alias;
import com.mirror.backend.api.dto.IotResponseUserDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseSummaryScheduleDto;
import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.entity.Mirror;
import com.mirror.backend.api.entity.RedisSummeryCalendar;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.repository.ConnectUserRepository;
import com.mirror.backend.api.repository.MirrorRepository;
import com.mirror.backend.api.repository.RedisSummeryCalendarRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.common.utils.IotEncryption;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Service
public class IotService {

    private MirrorRepository mirrorRepository;
    private UserRepository userRepository;
    private ConnectUserRepository connectUserRepository;
    private RedisSummeryCalendarRepository redisSummeryCalendarRepository;
    private RedisTemplate redisTemplate;
    private IotEncryption iotEncryption;

    private Long mirror_group_id;

    @Autowired
    public IotService(MirrorRepository mirrorRepository,
                      UserRepository userRepository,
                      ConnectUserRepository connectUserRepository,
                      RedisSummeryCalendarRepository redisSummeryCalendarRepository, RedisTemplate<String, String> redisTemplate, IotEncryption iotEncryption) {
        this.mirrorRepository = mirrorRepository;
        this.userRepository = userRepository;
        this.connectUserRepository = connectUserRepository;
        this.redisSummeryCalendarRepository = redisSummeryCalendarRepository;
        this.redisTemplate = redisTemplate;
        this.iotEncryption = iotEncryption;
    }


    public boolean findMirror(String encryptedCode){

        String mirrorId = iotEncryption.decryptionText(encryptedCode);
        Mirror mirror = mirrorRepository.findByMirrorId(mirrorId).orElseThrow( () -> new NoSuchFieldError());
        mirror_group_id = mirror.getMirrorGroupId();

        return true;
    }

    public List<IotResponseUserDto> fineUsersInfo(String encryptedCode) {

        List<User> usersInSameHouse = userRepository.findByHouseholdId(mirror_group_id);
        List<IotResponseUserDto> responseUserDtos = new ArrayList<>();

        for(User user : usersInSameHouse){

            List<Alias> aliases = findConnectUserAlias(user.getUserId());
            String imgData = findUserProfileImg(user.getUserEmail());

            IotResponseUserDto userDto = IotResponseUserDto.builder()
                    .userId(user.getUserId())
                    .userName(user.getUserName())
                    .userEmail(user.getUserEmail())
                    .aliases(aliases)
                    .profileImage(imgData)
                    .build();

            responseUserDtos.add(userDto);
        }
        return responseUserDtos;
    }

    private String findUserProfileImg(String userEmail){
        String key = "profileImg:" + userEmail;
        String value = (String) redisTemplate.opsForHash().get(key, "imageData");

        return value;
    }

    private List<Alias> findConnectUserAlias(Long userId){

        List<Alias> aliases = new ArrayList<>();
        List<ConnectUser> connectUsers = connectUserRepository.findByIdUserId(userId);

        for(ConnectUser connectUser : connectUsers){
            String connectUserEmail = findUserName(connectUser.getId().getConnectUserId());
            Alias alias = Alias.builder()
                    .connectUserEmail(connectUserEmail)
                    .connectUserAlias( connectUser.getConnectUserAlias())
                    .build();

            aliases.add(alias);
        }
        return aliases;
    }

    private String findUserName(Long userId){
        return userRepository.findByUserId(userId).get().getUserEmail();
    }


    public ResponseSummaryScheduleDto getSummerySchedule(String userEmail) {

        RedisSummeryCalendar redisSummeryCalendar = redisSummeryCalendarRepository.findById(userEmail)
                .orElseThrow( () -> new NoSuchElementException());

        ResponseSummaryScheduleDto dto = ResponseSummaryScheduleDto.builder()
                .summeryCalendarText(redisSummeryCalendar.getSummeryCalendar())
                .build();
        return dto;
    }
}
