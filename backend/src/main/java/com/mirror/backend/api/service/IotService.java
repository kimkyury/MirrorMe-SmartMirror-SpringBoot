package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.Alias;
import com.mirror.backend.api.dto.IotResponseUserDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseFamilyBirthdayScheduleDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseFirstMirrorTextDto;
import com.mirror.backend.api.dto.chatbotDtos.ResponseSummaryScheduleDto;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.common.utils.IotEncryption;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

@Service
@RequiredArgsConstructor
public class IotService {

    private final MirrorRepository mirrorRepository;
    private final UserRepository userRepository;
    private final ConnectUserRepository connectUserRepository;
    private final RedisSummeryCalendarRepository redisSummeryCalendarRepository;
    private final RedisFirstMirrorTextRepository redisFirstMirrorTextRepository;
    private final RedisFamilyBirthdayRepository redisFamilyBirthdayRepository;

    private final RedisTemplate redisTemplate;
    private final IotEncryption iotEncryption;


    public Long findMirrorGroupId(String encryptedCode){

        System.out.println("원본: " + encryptedCode);

//       TODO: Delete Encoding, Decoding Test Annotation

//        String encode= iotEncryption.encryptionText(encryptedCode);
//        System.out.println("암호화: " + encode);
//        String decode= iotEncryption.decryptionText(encode);
//        System.out.println("복호화: " + decode);
//        encryptedCode = encode;

        String mirrorId = iotEncryption.decryptionText(encryptedCode);
        System.out.println("해독된 mirrorID: " + mirrorId);

        Mirror mirror = mirrorRepository.findByMirrorId(mirrorId).orElseThrow(
                () -> new NoSuchElementException("해당 ID를 갖는 Mirror가 없습니다. "));

        return mirror.getMirrorGroupId();
    }

    public List<IotResponseUserDto> findUsersInfo(String encryptedCode) {

        Long mirrorGroupId = findMirrorGroupId(encryptedCode);
        List<User> usersInSameHouse = userRepository.findByHouseholdHouseholdId(mirrorGroupId);
        List<IotResponseUserDto> responseUserDtoList = new ArrayList<>();

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

            responseUserDtoList.add(userDto);
        }

        return responseUserDtoList;
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

    public ResponseFamilyBirthdayScheduleDto getBirthdayUserText(String userEmail) {

        RedisFamilyBirthday redisFamilyBirthday = redisFamilyBirthdayRepository.findById(userEmail)
                .orElseThrow( () -> new NoSuchElementException("생성된 생일관련 TEXT가 없습니다. "));

        ResponseFamilyBirthdayScheduleDto dto = ResponseFamilyBirthdayScheduleDto.builder()
                .familyBirthdayText(redisFamilyBirthday.getFamilyBirthday())
                .build();

        return dto;
    }

    public ResponseFirstMirrorTextDto getFirstMirrorTextDto(String userEmail){

        RedisMirrorFirstText redisMirrorFirstText = redisFirstMirrorTextRepository
                .findById(userEmail).orElseThrow(
                        () -> new NoSuchElementException("해당 유저는 최조Text를 갖고 있지 않습니다. ")
                );

        // 이미 사용된 Text일 경우
        if ( redisMirrorFirstText.getIsUsed().equals("1") )
            return null;

        redisMirrorFirstText.setIsUsed("1");
        redisFirstMirrorTextRepository.save(redisMirrorFirstText);

        ResponseFirstMirrorTextDto firstMirrorTextDto = ResponseFirstMirrorTextDto.builder()
                .textCode(redisMirrorFirstText.getTextCode())
                .textContent(redisMirrorFirstText.getTextContent())
                .build();

        return firstMirrorTextDto;
    }
}
