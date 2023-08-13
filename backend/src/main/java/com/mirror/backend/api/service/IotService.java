package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.Alias;
import com.mirror.backend.api.dto.UserDto;
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
    private final TextSummaryScheduleRepository textSummaryScheduleRepository;
    private final TextFirstMeetingRepository textFirstMeetingRepository;
    private final TextFamilyBirthdayRepository textFamilyBirthdayRepository;

    private final RedisTemplate redisTemplate;
    private final IotEncryption iotEncryption;


    public Long findMirrorGroupId(String encryptedCode){

        System.out.println("원본: " + encryptedCode);

//       TODO: Delete Encoding, Decoding Test Annotation

        String encode= iotEncryption.encryptionText(encryptedCode);
        System.out.println("암호화: " + encode);
        String decode= iotEncryption.decryptionText(encode);
        System.out.println("복호화: " + decode);
        encryptedCode = encode;

        String mirrorId = iotEncryption.decryptionText(encryptedCode);
        System.out.println("해독된 mirrorID: " + mirrorId);

        Mirror mirror = mirrorRepository.findByMirrorId(mirrorId).orElseThrow(
                () -> new NoSuchElementException("해당 ID를 갖는 Mirror가 없습니다. "));

        return mirror.getMirrorGroupId();
    }

    public List<UserDto.IotUsersRes> findUsersInfo(String encryptedCode) {

        Long mirrorGroupId = findMirrorGroupId(encryptedCode);
        List<User> usersInSameHouse = userRepository.findByHouseholdHouseholdId(mirrorGroupId);
        List<UserDto.IotUsersRes> iotUsersResList = new ArrayList<>();

        for(User user : usersInSameHouse){
            List<Alias> aliases = findConnectUserAlias(user.getUserId());
            String imgData = findUserProfileImg(user.getUserEmail());
            UserDto.IotUsersRes userDto = UserDto.IotUsersRes.builder()
                    .userId(user.getUserId())
                    .userName(user.getUserName())
                    .userEmail(user.getUserEmail())
                    .aliases(aliases)
                    .profileImage(imgData)
                    .build();

            iotUsersResList.add(userDto);
        }

        return iotUsersResList;
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

        TextSummarySchedule textSummarySchedule = textSummaryScheduleRepository.findById(userEmail)
                .orElseThrow( () -> new NoSuchElementException());

        ResponseSummaryScheduleDto dto = ResponseSummaryScheduleDto.builder()
                .summeryCalendarText(textSummarySchedule.getTextSummarySchedule())
                .build();

        return dto;
    }

    public ResponseFamilyBirthdayScheduleDto getBirthdayUserText(String userEmail) {

        TextFamilyBirthday textFamilyBirthday = textFamilyBirthdayRepository.findById(userEmail)
                .orElseThrow( () -> new NoSuchElementException("생성된 생일관련 TEXT가 없습니다. "));

        ResponseFamilyBirthdayScheduleDto dto = ResponseFamilyBirthdayScheduleDto.builder()
                .familyBirthdayText(textFamilyBirthday.getTextFamilyBirthday())
                .build();

        return dto;
    }

    public ResponseFirstMirrorTextDto getFirstMirrorTextDto(String userEmail){

        TextFirstMeeting textFirstMeeting = textFirstMeetingRepository
                .findById(userEmail).orElseThrow(
                        () -> new NoSuchElementException("해당 유저는 최조Text를 갖고 있지 않습니다. ")
                );

        // 이미 사용된 Text일 경우
        if ( textFirstMeeting.getIsUsed().equals("1") )
            return null;

        textFirstMeeting.setIsUsed("1");
        textFirstMeetingRepository.save(textFirstMeeting);

        ResponseFirstMirrorTextDto firstMirrorTextDto = ResponseFirstMirrorTextDto.builder()
                .textCode(textFirstMeeting.getTextCode())
                .textContent(textFirstMeeting.getTextContent())
                .build();

        return firstMirrorTextDto;
    }
}
