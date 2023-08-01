package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
public class RequestCreateUserDto {

    private String userName;
    private String userNickname;
    private List<Long> interestCodes;
    private Long householdId;

    @Override
    public String toString() {
        return "RequestCreateUserDto{" +
                "userName='" + userName + '\'' +
                ", userNickname='" + userNickname + '\'' +
                ", interestCodes=" + interestCodes +
                ", householdId=" + householdId +
                '}';
    }
}
