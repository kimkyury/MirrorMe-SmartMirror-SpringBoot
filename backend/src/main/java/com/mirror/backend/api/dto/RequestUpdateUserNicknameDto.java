package com.mirror.backend.api.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class RequestUpdateUserNicknameDto {

    String userNickname;



    @Override
    public String toString() {
        return "RequestUpdateUserNicknameDto{" +
                "userNickname='" + userNickname + '\'' +
                '}';
    }
}
