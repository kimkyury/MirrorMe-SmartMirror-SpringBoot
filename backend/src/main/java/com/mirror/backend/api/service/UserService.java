package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.RequestCreateUserDto;
import com.mirror.backend.api.dto.RequestInterestDto;
import com.mirror.backend.api.dto.RequestUpdateUserNicknameDto;
import com.mirror.backend.api.dto.ResponseInterestDto;
import com.mirror.backend.api.entity.Interest;
import com.mirror.backend.api.entity.InterestCommonCode;
import com.mirror.backend.api.entity.User;
import com.mirror.backend.api.entity.keys.InterestKey;
import com.mirror.backend.api.repository.InterestCommonCodeRepository;
import com.mirror.backend.api.repository.InterestsRepository;
import com.mirror.backend.api.repository.UserRepository;
import com.mirror.backend.common.utils.Constants.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.server.ResponseStatusException;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final InterestsRepository interestRepository;
    private final InterestCommonCodeRepository interestCommonCodeRepository;

    @Autowired
    public UserService(UserRepository userRepository, InterestsRepository interestRepository,
                           InterestCommonCodeRepository interestCommonCodeRepository) {
        this.userRepository = userRepository;
        this.interestRepository = interestRepository;
        this.interestCommonCodeRepository = interestCommonCodeRepository;
    }


    int SUCCESS = 1;
    int FAIL = 0;

    public User getUser(Long userId) {
        return userRepository.findById(userId)
                .orElseThrow(() ->
                        new ResponseStatusException(HttpStatus.NOT_FOUND, "User not found"));
    }

    public User createUser(String userEmail){
        User user = new User();
        user.setUserEmail(userEmail);
        return userRepository.save(user);
    }

    public int updateInitUser(String userEmail, Long userId, RequestCreateUserDto requestCreateUserDto ){

        Optional<User> user = userRepository.findByUserEmail(userEmail);
        // userId찾기

        if ( user.isEmpty())
            return FAIL;

        String userName = requestCreateUserDto.getUserName();
        String userNickname = requestCreateUserDto.getUserNickname();
        List<Long> interestCodes = requestCreateUserDto.getInterestCodes();
        Long householdId = requestCreateUserDto.getHouseholdId();

        // 저장된 파일의 경로를 DB에 저장

        // uesrTable Update
        user.ifPresent(selectUser -> {
            selectUser.setUserName(userName);
            selectUser.setUserNickname(userNickname);
            selectUser.setHouseholdId(householdId);
            selectUser.setCreateAt(LocalDateTime.now());
            userRepository.save(selectUser);
        });

        // interests Create (multyKey1; userId, multiKey2: interestId)
        // 복합키 이용
        for(int i =0; i<interestCodes.size(); i++){
            InterestKey interestKey = new InterestKey();
            interestKey.setUserId(userId);
            interestKey.setInterestCode(interestCodes.get(i));

            Interest interest = new Interest();
            interest.setId(interestKey);
            interest.setIsUsed(1);

            interestRepository.save(interest);
        }

        return SUCCESS;
    }



    public int uploadProfileImage(String userEmail,  MultipartFile file) {
        Optional<User> user = userRepository.findByUserEmail(userEmail);

        String UPLOAD_DIR = "ImgTest/";  //TODO: 서버내의 절대경로로 바꿀 것

        Path filePath = null;

        try {

            Path resourceDirectory = Paths.get("src","main","resources", UPLOAD_DIR);
            String absolutePath = resourceDirectory.toFile().getAbsolutePath();

            filePath = Paths.get(absolutePath, file.getOriginalFilename());
            Files.write(filePath, file.getBytes());

        } catch (IOException e) {
            // 에러 처리
            e.printStackTrace();
        }

        System.out.println("이미지파일 저장경로: " + filePath.toString());
        Path finalFilePath = filePath;

        user.ifPresent(selectUser -> {
            selectUser.setProfileImageUrl(finalFilePath.toString());
            selectUser.setModifiedAt(LocalDateTime.now());
            userRepository.save(selectUser);
        });

        return Result.SUCCESS;
    }

    public boolean isExistUser(String email){

        Optional<User> user = userRepository.findByUserEmail(email);
        if(user.isEmpty()) return false;

        return true;
    }

    public List<ResponseInterestDto> getInterestDtoList(String userEmail, Long userId) {
        Optional<User> user = userRepository.findByUserEmail(userEmail);

        List<Interest> interests = interestRepository.findByIdUserIdAndIsUsed(userId, 1);
        List<InterestCommonCode> interestCodes = interestCommonCodeRepository.findAll();

        HashMap<Long, String> interestCodesMap = new HashMap<>();
        for( InterestCommonCode interestCode : interestCodes ){
            interestCodesMap.put(interestCode.getInterestCode(), interestCode.getInterestName());
        }

        List<ResponseInterestDto> responseInterestDtoList= new ArrayList<>();
        for(Interest interest : interests){
            Long interestCode = interest.getId().getInterestCode();
            String interestName = interestCodesMap.get(interestCode);
            ResponseInterestDto dto = new ResponseInterestDto(interestCode, interestName);
            responseInterestDtoList.add(dto);
        }
        return responseInterestDtoList;

    }

    public int updateInterest(String userEmail, Long userId, RequestInterestDto requestInterestDto) {

        int INTEREST_CREATED = 2;
        int INTEREST_OFF = 0;
        int INTEREST_ON = 1;


        Optional<User> user = userRepository.findByUserEmail(userEmail);

        Long interestCode = requestInterestDto.getInterestCode();
        Optional<Interest> interestOptional = interestRepository.findByIdUserIdAndIdInterestCode(userId, interestCode);

        // 애초에 조회할 수 없는 애라면, userId와 code를 복합키로하여 생성한다
        if (interestOptional.isEmpty()){
            InterestKey interestKey = new InterestKey( userId, interestCode);
            Interest interest = Interest.builder()
                    .id(interestKey)
                    .isUsed(1)
                    .build();
            interestRepository.save(interest);
            return INTEREST_CREATED;
        }

        // dto에 대하여, 이미 1이라면 0으로 만들고, 이미 0이라면 1로 만든다

        interestOptional.ifPresent(selectInterest -> {
            if ( selectInterest.getIsUsed() == INTEREST_OFF){
                selectInterest.setIsUsed(INTEREST_ON);
                interestRepository.save(selectInterest);
            }else{
                selectInterest.setIsUsed(INTEREST_OFF);
                interestRepository.save(selectInterest);
            }
        });



        return interestOptional.get().getIsUsed();
    }

    public String getUserProfileImage(Long userId) {

        Optional<User> user = userRepository.findByUserId(userId);
        if ( user.isEmpty()){
            return "FAIL";
        }
        return user.get().getProfileImageUrl();
    }

    public int deleteUser(Long userId) {

        try {
            userRepository.deleteById(userId);
        } catch(Exception e){
            e.getMessage();
            return Result.FAIL;
        }
        return Result.SUCCESS;
    }

    public int updateUserNickname(Long userId, RequestUpdateUserNicknameDto dto) {

        Optional<User> user = userRepository.findByUserId(userId);

        user.ifPresent( selectUser -> {
           selectUser.setUserNickname(dto.getUserNickname());
           userRepository.save(selectUser);
        });

        return Result.SUCCESS;
    }
}
