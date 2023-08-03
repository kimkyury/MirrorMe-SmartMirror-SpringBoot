package com.mirror.backend.api.dto;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ResponseHouseholdDto {
    private String householdName;
    private Long householdId;
    private String createUserName;
    private String createUserEmail;


    @Builder
    public ResponseHouseholdDto(String householdName, Long householdId, String createUserName, String createUserEmail) {
        this.householdName = householdName;
        this.householdId = householdId;
        this.createUserName = createUserName;
        this.createUserEmail = createUserEmail;
    }


    @Override
    public String toString() {
        return "ResponseSearchHouseholdDto{" +
                "householdName='" + householdName + '\'' +
                ", householdId='" + householdId + '\'' +
                ", createUser='" + createUserName + '\'' +
                ", createUserEmail='" + createUserEmail + '\'' +
                '}';
    }

}
