package com.mirror.backend.api.dto;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

public class HouseholdDto {

    @Getter
    @Setter
    @ToString
    public static class HouseholdReq{

        private String householdName;
    }

    @Getter
    @ToString
    public static class HouseholdPostRes{

        private Long householdId;
        private String householdName;
        private String createUserName;  // TODO: createNAme, CreateUserEmail은 사용되지 않는다면 삭제예정
        private String createUserEmail;

        @Builder
        public HouseholdPostRes(String householdName, Long householdId, String createUserName, String createUserEmail) {
            this.householdName = householdName;
            this.householdId = householdId;
            this.createUserName = createUserName;
            this.createUserEmail = createUserEmail;
        }
    }

    @Getter
    @ToString
    public static class HouseHoldGetRes{
        private Long householdId;
        private String householdName;
        private String createUserName;
        private String createUserEmail;

        @Builder
        public HouseHoldGetRes(String householdName, Long householdId, String createUserName, String createUserEmail) {
            this.householdName = householdName;
            this.householdId = householdId;
            this.createUserName = createUserName;
            this.createUserEmail = createUserEmail;
        }
    }
}
