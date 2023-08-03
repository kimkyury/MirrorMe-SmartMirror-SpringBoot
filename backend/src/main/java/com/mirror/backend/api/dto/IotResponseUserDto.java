package com.mirror.backend.api.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.List;


@Getter
@Setter
public class IotResponseUserDto {

    Long userId;
    String userName;
    String userEmail;
    String profileImage;
    List<Alias> aliases;

    @Builder
    public IotResponseUserDto(Long userId, String userName, String userEmail, String profileImage, List<Alias> aliases) {
        this.userId = userId;
        this.userName = userName;
        this.userEmail = userEmail;
        this.profileImage = profileImage;
        this.aliases = aliases;
    }

    @Override
    public String toString() {
        return "IotResponseUsersDto{" +
                "userId=" + userId +
                ", userName='" + userName + '\'' +
                ", userEmail='" + userEmail + '\'' +
                ", profileImage='" + profileImage + '\'' +
                ", aliases=" + aliases +
                '}';
    }
}
