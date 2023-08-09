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

        System.out.println("원본: " + encryptedCode);
        String mirrorId = iotEncryption.decryptionText(encryptedCode);
        System.out.println("디코딩: " + iotEncryption.decryptionText(encryptedCode));

        Mirror mirror = mirrorRepository.findByMirrorId(mirrorId).orElseThrow( () -> new NoSuchFieldError());
        System.out.println(mirror);

        mirror_group_id = mirror.getMirrorGroupId();

        return true;
    }

    public List<IotResponseUserDto> fineUsersInfo(String encryptedCode) {

        // 1. Mirror 테이블에서 해당 Mirrorid를 찾아온다
//        String mirrorId = iotEncryption.decryptionText(encryptedCode);
//        String mirrorId = encryptedCode
        //TODO:암호화

        // 2. {mirrorId}의 {mirror_group_id}를 찾아온다


        // 3. {mirror_group_id}를 가지고 users에서 user들을 찾아온다
        List<User> usersInSameHouse = userRepository.findByHouseholdId(mirror_group_id);
        List<IotResponseUserDto> responseUserDtos = new ArrayList<>();


        for(User user : usersInSameHouse){
            // 친인척 별명들 찾기
            List<Alias> aliases = findConnectUserAlias(user.getUserId());

            // 프로필 이미지 꺼내기
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

        // 4. userList 각각에 대하여 userEmail을 통해 Redis내의 Profile을 가져온다
        // 5. encoding된 profile이미지를 Response에 담는다
        // 6. 해당값을 Json파일로 묶어서 내보낸다


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


        Optional<RedisSummeryCalendar> redisSummeryCalendar = redisSummeryCalendarRepository.findById(userEmail);

        if (redisSummeryCalendar.isEmpty()){
            return null;
        }

        ResponseSummaryScheduleDto dto = ResponseSummaryScheduleDto.builder()
                .summeryCalendarText(redisSummeryCalendar.get().getSummeryCalendar())
                .build();

        return dto;

    }
}
