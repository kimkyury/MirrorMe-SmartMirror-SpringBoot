package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;


@Getter
@Setter
public class ResponseUserInfoDto {

    @JsonProperty("userEmail")
    private String userEmail;

    @JsonProperty("userName")
    private String userName;

    @JsonProperty("createAt")
    private LocalDateTime createAt;

    @JsonProperty("modifiedAt")
    private LocalDateTime modifiedAt;

    @JsonProperty("householdId")
    private Long householdId;

    @Builder
    public ResponseUserInfoDto(String userEmail, String userName, LocalDateTime createAt, LocalDateTime modifiedAt, Long householdId) {
        this.userEmail = userEmail;
        this.userName = userName;
        this.createAt = createAt;
        this.modifiedAt = modifiedAt;
        this.householdId = householdId;
    }

    @Override
    public String toString() {
        return "ResponseUserInfoDto{" +
                ", userEmail='" + userEmail + '\'' +
                ", userName='" + userName + '\'' +
                ", createAt=" + createAt +
                ", modifiedAt=" + modifiedAt +
                ", householdId=" + householdId +
                '}';
    }
}
