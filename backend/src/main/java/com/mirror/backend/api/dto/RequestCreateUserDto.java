package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
public class RequestCreateUserDto {

    private String userName;
    private List<Long> interestCodes;

    @Override
    public String toString() {
        return "RequestCreateUserDto{" +
                "userName='" + userName + '\'' +
                ", interestCodes=" + interestCodes +
                '}';
    }
}
