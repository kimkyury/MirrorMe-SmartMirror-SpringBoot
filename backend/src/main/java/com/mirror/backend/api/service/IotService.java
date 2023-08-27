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

public interface IotService {

    public Long findMirrorGroupId(String encryptedCode);

    public FileInputStream getVideoDetail(Long videoId) throws FileNotFoundException;

    public List<UserDto.IotUsersRes> findUsersInfo(String encryptedCode);

    public TextSummaryScheduleDto getSummerySchedule(String userEmail) ;

    public TextFamilyBirthdayDto getBirthdayUserText(String userEmail);

    public TextVideoViewDto getTextVideoViewText(String userEmail);

    public TextEmotionBasedContactRecommendationDto getTextEmotionBasedContactRecommendationText(String userEmail);

    public TextFirstMeetingDto getFirstMirrorTextDto(String userEmail);

    public TextCautionRainyDto getCautionRainyText(String userEmail);
}
