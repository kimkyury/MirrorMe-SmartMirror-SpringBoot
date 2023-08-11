package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.Alias;
import com.mirror.backend.api.dto.IotResponseUserDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseFirstMirrorTextDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseSummaryScheduleDto;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.repository.*;
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
    private RedisFirstMirrorTextRepository redisFirstMirrorTextRepository;

    private RedisTemplate redisTemplate;
    private IotEncryption iotEncryption;

    private Long mirror_group_id;

    @Autowired
    public IotService(MirrorRepository mirrorRepository,
                      UserRepository userRepository,
                      ConnectUserRepository connectUserRepository,
                      RedisSummeryCalendarRepository redisSummeryCalendarRepository,
                      RedisFirstMirrorTextRepository redisFirstMirrorTextRepository,
                      RedisTemplate<String, String> redisTemplate,
                      IotEncryption iotEncryption) {
        this.mirrorRepository = mirrorRepository;
        this.userRepository = userRepository;
        this.connectUserRepository = connectUserRepository;
        this.redisSummeryCalendarRepository = redisSummeryCalendarRepository;
        this.redisFirstMirrorTextRepository = redisFirstMirrorTextRepository;
        this.redisTemplate = redisTemplate;
        this.iotEncryption = iotEncryption;
    }


    public boolean findMirror(String encryptedCode){

        System.out.println("원본: " + encryptedCode);
////
// //       TODO: 주석삭제
//        String encode= iotEncryption.encrytionText(encryptedCode);
//        System.out.println("암호화: " + encode);
//        String decode= iotEncryption.decryptionText(encode);
//        System.out.println("복호화: " + decode);
//        encryptedCode = encode;

        String mirrorId = iotEncryption.decryptionText(encryptedCode);
        System.out.println("해독된 mirrorID: " + mirrorId);
        Mirror mirror = mirrorRepository.findByMirrorId(mirrorId).orElseThrow( () -> new NoSuchFieldError());
        mirror_group_id = mirror.getMirrorGroupId();

        return true;
    }


    public void UnicodeConversion() {
        int unicodeCodePoint = 128514; // An emoji's unicode code point
        String character = new String(Character.toChars(unicodeCodePoint));
        System.out.println(character); // 출력: 😂
    }


    public List<IotResponseUserDto> fineUsersInfo(String encryptedCode) {

        List<User> usersInSameHouse = userRepository.findByHouseholdHouseholdId(mirror_group_id);
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

    public ResponseFirstMirrorTextDto getFirstMirrorTextDto(String userEmail){
        // 하루 중, 최초 유저 만남 시 뱉을 Text

        // TODO: 배포환경에서는 해당 값이 그냥 바로 삭제 됨
        //  3. 해당 유저의 Text가 이미 사용된 값이라면 return null을 한다

        // 3. 해당 유저의 Data의 출력물이 존재한다면 ResponseFirstMirrorTextDto를 만든다

        System.out.println(userEmail);
        RedisMirrorFirstText redisMirrorFirstText = redisFirstMirrorTextRepository
                .findById(userEmail).orElseThrow( () -> new NoSuchElementException());

        if ( redisMirrorFirstText.getIsUsed().equals("1") ){
            // 이미 사용된 Text일 경우
            return null;
        }

        // 사용했다고 설정
        redisMirrorFirstText.setIsUsed("1");
        redisFirstMirrorTextRepository.save(redisMirrorFirstText);

        ResponseFirstMirrorTextDto firstMirrorTextDto = ResponseFirstMirrorTextDto.builder()
                .textCode(redisMirrorFirstText.getTextCode())
                .textContent(redisMirrorFirstText.getTextContent())
                .build();

        return firstMirrorTextDto;

    }
}
