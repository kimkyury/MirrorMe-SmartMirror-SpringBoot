package com.mirror.backend.api.service.impl;

import com.mirror.backend.api.dto.EmotionCountDto;
import com.mirror.backend.api.dto.EmotionDto;
import com.mirror.backend.api.dto.UserDto;
import com.mirror.backend.api.entity.*;
import com.mirror.backend.api.entity.keys.EmotionKey;
import com.mirror.backend.api.repository.ConnectUserRepository;
import com.mirror.backend.api.repository.EmotionCountRepository;
import com.mirror.backend.api.repository.EmotionRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.api.service.EmotionService;
import com.mirror.backend.common.exception.NotFoundException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class EmotionServiceImpl implements EmotionService {

    @Autowired
    private EmotionRepository emotionRepository;

    @Autowired
    private EmotionCountRepository emotionCountRepository;

    @Autowired
    private ConnectUserRepository connectUserRepository;

    @Autowired
    private UserRepository userRepository;

    private final Logger logger = LoggerFactory.getLogger(getClass());

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long saveEmotion(EmotionDto.EmotionReq emotionReq) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd");
        LocalDate date = LocalDate.parse(emotionReq.getEmotionDate(), formatter);

        Optional<Emotion> isEmotion = emotionRepository.findByEmotionDateAndUserId(date, emotionReq.getUserId());
        Long res = null;
        if(isEmotion.isPresent()) {
            hasEmotion(isEmotion.get(), emotionReq);
            res = isEmotion.get().getEmotionId();
        }
        else {
            res = hasNoEmotion(date, emotionReq);
        }
        return res;
    }

    @Transactional(rollbackFor = Exception.class)
    public void hasEmotion(Emotion emotion, EmotionDto.EmotionReq emotionReq) {
        List<Integer> emotionList = emotionReq.getEmotionList();
        for(int i=1; i<emotionList.size(); i++) {
            Integer myEmotion = emotionList.get(i);
            if(myEmotion == 0) continue;

            Optional<EmotionCount> isPresentEmotionCode = emotionCountRepository.findByEmotionKeyEmotionIdAndEmotionKeyEmotionCode(emotion.getEmotionId(), i);

            EmotionCount emotionCount = null;
            if(isPresentEmotionCode.isPresent()) {
                 emotionCount = isPresentEmotionCode.get();
                int plusCount = emotionCount.getEmotionCount() + myEmotion;
                emotionCount.update(plusCount);
                emotionCountRepository.save(emotionCount);
            }
            else {
                EmotionKey emotionKey = EmotionKey.builder()
                        .emotionId(emotion.getEmotionId())
                        .emotionCode(i)
                        .build();

                emotionCount = EmotionCount.builder()
                        .emotionKey(emotionKey)
                        .emotionCount(myEmotion).build();

                emotionCountRepository.save(emotionCount);
            }
        }
    }

    @Transactional(rollbackFor = Exception.class)
    public Long hasNoEmotion(LocalDate date, EmotionDto.EmotionReq emotionReq) {
        Emotion emotion = Emotion.builder()
                .emotionDate(date)
                .emotionCode(0)
                .userId(emotionReq.getUserId())
                .createAt(LocalDateTime.now())
                .build();
        Emotion emotionEntity = emotionRepository.save(emotion);

        List<Integer> emotionList = emotionReq.getEmotionList();
        for(int i=1; i<emotionList.size(); i++) {
            Integer myEmotion = emotionList.get(i);
            if(myEmotion == 0) continue;

            EmotionKey emotionKey = EmotionKey.builder()
                    .emotionId(emotionEntity.getEmotionId())
                    .emotionCode(i)
                    .build();

            EmotionCount emotionCount = EmotionCount.builder()
                    .emotionKey(emotionKey)
                    .emotionCount(myEmotion).build();

            emotionCountRepository.save(emotionCount);
        }

        return emotionEntity.getEmotionId();
    }

    @Override
    public List<EmotionDto.EmotionRes> getMyEmotion(Long userId) {
        // 일주일간의 감정 보여주기
        LocalDate oneDayAge = LocalDate.now().minusDays(1);
        LocalDate eightDayAgo = LocalDate.now().minusDays(8);

        List<Emotion> myEmotionList = emotionRepository.findAllByEmotionDateBetweenAndUserId(eightDayAgo, oneDayAge, userId);

        // emotion 1개당 emotion count 조회
        List<EmotionDto.EmotionRes> emotionResList = new ArrayList<>();
        for(Emotion emotion: myEmotionList) {
            Long emotionId = emotion.getEmotionId();
            List<EmotionCount> emotionCountList = emotionCountRepository.findAllByEmotionKeyEmotionId(emotionId);
            List<EmotionCountDto.EmotionCountRes> transformCountList = emotionCountList.stream().map(EmotionCountDto.EmotionCountRes::new)
                    .collect(Collectors.toList());

            EmotionDto.EmotionRes emotionOneDay = EmotionDto.EmotionRes.builder()
                    .emotionDate(emotion.getEmotionDate().toString())
                    .emotionList(transformCountList)
                    .build();
            emotionResList.add(emotionOneDay);
        }
        return emotionResList;
    }

    @Override
    public List<EmotionDto.EmotionFamilyResList> getFamilyEmotion(Long userId) {
        LocalDate oneDayAge = LocalDate.now().minusDays(1);
        LocalDate eightDayAgo = LocalDate.now().minusDays(8);

        List<ConnectUser> familyId = connectUserRepository.findByIdUserId(userId);
        System.out.println("familyId.size() = " + familyId.size());

        List<EmotionDto.EmotionFamilyResList> emotionFamilyResLists = new ArrayList<>();
        for(ConnectUser user: familyId) {
            Long connectUserId = user.getId().getConnectUserId();
            String connectUserAlias = user.getConnectUserAlias();

            List<Emotion> myEmotionList = emotionRepository.findAllByEmotionDateBetweenAndUserId(eightDayAgo, oneDayAge, connectUserId);

            List<EmotionDto.EmotionRes> emotionResList = new ArrayList<>();
            for(Emotion emotion: myEmotionList) {
                Long emotionId = emotion.getEmotionId();
                List<EmotionCount> emotionCountList = emotionCountRepository.findAllByEmotionKeyEmotionId(emotionId);
                List<EmotionCountDto.EmotionCountRes> transformCountList = emotionCountList.stream().map(EmotionCountDto.EmotionCountRes::new)
                        .collect(Collectors.toList());

                EmotionDto.EmotionRes emotionOneDay = EmotionDto.EmotionRes.builder()
                        .emotionDate(emotion.getEmotionDate().toString())
                        .emotionList(transformCountList)
                        .build();
                emotionResList.add(emotionOneDay);
            }
            emotionFamilyResLists.add(EmotionDto.EmotionFamilyResList.builder()
                    .connectUserAlias(connectUserAlias)
                    .emotionList(emotionResList)
                    .build());
        }
        return emotionFamilyResLists;
    }

    @Override
    public List<UserDto> familyAngryList(Long userId) {
        LocalDate oneDayAgo = LocalDate.now().minusDays(1);

        List<UserDto> userList = new ArrayList<>();
        List<ConnectUser> familyId = connectUserRepository.findByIdUserId(userId);
        logger.info(familyId.toString());
        for(ConnectUser connectUser : familyId) {
            Long connectUserId = connectUser.getId().getConnectUserId();
            User user = userRepository.findByUserId(connectUserId).orElseThrow(() -> new NotFoundException("사용자가 없습니다."));

            Optional<Emotion> emotion = emotionRepository.findByEmotionDateAndUserId(oneDayAgo, connectUserId);

            if(emotion.isPresent()) {
                if(emotion.get().getEmotionCode() == 3 || emotion.get().getEmotionCode() == 4) {
                    UserDto userDto = new UserDto(user);
                    userList.add(userDto);
                }
            }
        }
        return userList;
    }
}
