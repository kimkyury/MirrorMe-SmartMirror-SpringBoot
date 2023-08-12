package com.mirror.backend.api.dto;

import com.mirror.backend.api.entity.Household;
import com.mirror.backend.api.entity.User;
import lombok.Getter;

import java.time.LocalDateTime;

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
