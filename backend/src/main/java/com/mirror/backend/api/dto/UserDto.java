package com.mirror.backend.api.dto;

import com.mirror.backend.api.entity.Household;
import com.mirror.backend.api.entity.User;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import javax.validation.constraints.NotNull;
import java.time.LocalDateTime;
import java.util.List;

@Getter
public class UserDto {

    private Long userId;
    private String userEmail;
    private String userName;
    private String password;
    private String createAt;
    private String modifiedAt;
    private HouseHoldDto household;
    private String birthday;

    public UserDto(User user) {
        this.userId = user.getUserId();
        this.userEmail = user.getUserEmail();
        this.userName = user.getUserName();
        this.password = user.getPassword();
        this.createAt = user.getCreateAt().toString();
        this.modifiedAt = user.getModifiedAt().toString();
        this.household = new HouseHoldDto(user.getHousehold());
        this.birthday = user.getBirthday();
    }

    @Getter
    @Setter
    @ToString
    public static class UserInitInfoReq{

        @NotNull
        private String userName;
        @NotNull
        private List<Long> interestCodes;
    }

    @Getter
    @Setter
    @ToString
    public static class UserSavePasswordReq{

        @NotNull
        private String userEmail;
        @NotNull
        private String password;
    }

    @Getter
    @ToString
    public static class UserInfoRes{

        private String userEmail;
        private String userName;
        private LocalDateTime createAt;
        private LocalDateTime modifiedAt;
        private Long householdId;

        @Builder
        public UserInfoRes(String userEmail, String userName, LocalDateTime createAt, LocalDateTime modifiedAt, Long householdId) {
            this.userEmail = userEmail;
            this.userName = userName;
            this.createAt = createAt;
            this.modifiedAt = modifiedAt;
            this.householdId = householdId;
        }
    }

    @Getter
    @Setter
    @ToString
    public static class IotUsersReq{

        @NotNull
        private String mirrorId;
    }

    @Getter
    @ToString
    public static class IotUsersRes{
        private Long userId;
        private String userName;
        private String userEmail;
        private String profileImage;
        private List<Alias> aliases;

        @Builder
        public IotUsersRes(Long userId, String userName, String userEmail, String profileImage, List<Alias> aliases) {
            this.userId = userId;
            this.userName = userName;
            this.userEmail = userEmail;
            this.profileImage = profileImage;
            this.aliases = aliases;
        }
    }

    @Getter
    public static class HouseHoldDto {

        Long householdId;
        String householdName;
        int gridNx;
        int gridNy;
        String region;

        public HouseHoldDto(Household household) {
            this.householdId = household.getHouseholdId();
            this.householdName = household.getHouseholdName();
            this.gridNx = household.getGridNx();
            this.gridNy = household.getGridNy();
            this.region = household.getRegion();
        }
    }
}
