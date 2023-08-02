package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;


@Getter
@Setter
public class ResponseUserInfoDto {

    @JsonProperty("userNickname")
    private String userNickname;

    @JsonProperty("userEmail")
    private String userEmail;

    @JsonProperty("userName")
    private String userName;

    @JsonProperty("profileImageUrl")
    private String profileImageUrl;

    @JsonProperty("createAt")
    private LocalDateTime createAt;

    @JsonProperty("modifiedAt")
    private LocalDateTime modifiedAt;

    @JsonProperty("householdId")
    private Long householdId;


    @Builder
    public ResponseUserInfoDto(String userNickname, String userEmail, String userName, String profileImageUrl, LocalDateTime createAt, LocalDateTime modifiedAt, Long householdId) {
        this.userNickname = userNickname;
        this.userEmail = userEmail;
        this.userName = userName;
        this.profileImageUrl = profileImageUrl;
        this.createAt = createAt;
        this.modifiedAt = modifiedAt;
        this.householdId = householdId;
    }

    @Override
    public String toString() {
        return "ResponseUserInfo{" +
                "userNickname='" + userNickname + '\'' +
                ", userEmail='" + userEmail + '\'' +
                ", userName='" + userName + '\'' +
                ", profileImageUrl='" + profileImageUrl + '\'' +
                ", createAt=" + createAt +
                ", modifiedAt=" + modifiedAt +
                ", householdId=" + householdId +
                '}';
    }
}
