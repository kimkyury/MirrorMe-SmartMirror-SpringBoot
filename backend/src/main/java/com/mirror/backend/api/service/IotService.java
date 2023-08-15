package com.mirror.backend.api.service;


import com.mirror.backend.api.dto.Alias;
import com.mirror.backend.api.dto.TextDto.*;
import com.mirror.backend.api.dto.UserDto;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.repository.*;
import com.mirror.backend.common.exception.NotFoundException;
import com.mirror.backend.common.utils.IotEncryption;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.HashOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class IotService {

    private final MirrorRepository mirrorRepository;
    private final UserRepository userRepository;
    private final ConnectUserRepository connectUserRepository;
    private final TextSummaryScheduleRepository textSummaryScheduleRepository;
    private final TextFirstMeetingRepository textFirstMeetingRepository;
    private final TextFamilyBirthdayRepository textFamilyBirthdayRepository;
    private final TextCautionRainyRepository textCautionRainyRepository;
    private final TextVideoViewRepository textVideoViewRepository;
    private final TextEmotionBasedContactRecommendationRepository textEmotionBasedContactRecommendationRepository;
    private final VideoRepository videoRepository;

    private final VideoService videoService;
    private final RedisTemplate redisTemplate;
    private final IotEncryption iotEncryption;



    public Long findMirrorGroupId(String encryptedCode){

        System.out.println("원본: " + encryptedCode);
//
////       TODO: Delete Encoding, Decoding Test Annotation
//
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

    public FileInputStream getVideoDetail(Long videoId) throws FileNotFoundException {
        VideoMessage videoMessage = videoRepository.findByVideoId(videoId)
                .orElseThrow(() -> new NotFoundException("Not Found Video"));
        videoMessage.update('Y');
        videoRepository.save(videoMessage);

        String videoUrl = videoService.getStringFromHash(videoMessage.getSendUserEmail(), videoId +"");
        return new FileInputStream(videoUrl);
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


    public TextSummaryScheduleDto getSummerySchedule(String userEmail) {

        Optional<TextSummarySchedule> textSummaryScheduleOptional = textSummaryScheduleRepository.findById(userEmail);
        if ( textSummaryScheduleOptional.isEmpty()) return null;

        TextSummaryScheduleDto dto = TextSummaryScheduleDto.builder()
                .text(textSummaryScheduleOptional.get().getTextSummarySchedule())
                .build();

        return dto;
    }

    public TextFamilyBirthdayDto getBirthdayUserText(String userEmail) {

        Optional<TextFamilyBirthday> textFamilyBirthdayOptional = textFamilyBirthdayRepository.findById(userEmail);
        if( textFamilyBirthdayOptional.isEmpty()) return null;

        TextFamilyBirthdayDto dto = TextFamilyBirthdayDto.builder()
                .text(textFamilyBirthdayOptional.get().getTextFamilyBirthday())
                .build();

        return dto;
    }

    public TextVideoViewDto getTextVideoViewText(String userEmail) {

        Optional<TextVideoView> textVideoViewOptional = textVideoViewRepository.findById(userEmail);
        if (textVideoViewOptional.isEmpty()) return null;

        TextVideoViewDto dto = TextVideoViewDto.builder()
                .text(textVideoViewOptional.get().getTextVideoView())
                .build();

        return dto;
    }

    public TextEmotionBasedContactRecommendationDto getTextEmotionBasedContactRecommendationText(String userEmail) {

        Optional<TextEmotionBasedContactRecommendation> textEmotionBasedContactRecommendationOptional
                = textEmotionBasedContactRecommendationRepository.findById(userEmail);
        if ( textEmotionBasedContactRecommendationOptional.isEmpty()) return null;

        TextEmotionBasedContactRecommendationDto dto = TextEmotionBasedContactRecommendationDto.builder()
                .text(textEmotionBasedContactRecommendationOptional.get()
                .getTextEmotionBasedContactRecommendation())
                .build();

        return dto;
    }

    public TextFirstMeetingDto getFirstMirrorTextDto(String userEmail){

        TextFirstMeeting textFirstMeeting = textFirstMeetingRepository
                .findById(userEmail).orElseThrow(
                        () -> new NoSuchElementException("해당 유저는 최조Text를 갖고 있지 않습니다. ")
                );

        // 이미 사용된 Text일 경우
        if ( textFirstMeeting.getIsUsed().equals("1") )
            return null;

        textFirstMeeting.setIsUsed("1");
        textFirstMeetingRepository.save(textFirstMeeting);

        TextFirstMeetingDto firstMirrorTextDto = TextFirstMeetingDto.builder()
                .textCode(textFirstMeeting.getTextCode())
                .textContent(textFirstMeeting.getTextContent())
                .build();

        return firstMirrorTextDto;
    }

    public TextCautionRainyDto getCautionRainyText(String userEmail) {

        Long householdId = userRepository.findByUserEmail(userEmail).get().getHousehold().getHouseholdId();
        TextCautionRainy textCautionRainy = textCautionRainyRepository.findById(String.valueOf(householdId)).get();

        TextCautionRainyDto textCautionRainyDto = TextCautionRainyDto.builder()
                .text(textCautionRainy.getTextCautionRainy())
                .build();

        return textCautionRainyDto;

    }
}
