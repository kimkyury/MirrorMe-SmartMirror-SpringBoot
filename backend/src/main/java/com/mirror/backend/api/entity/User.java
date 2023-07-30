package com.mirror.backend.api.entity;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;

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

    @JsonProperty("roleType")
    private String roleType;


    @Override
    public String toString() {
        return "User{" +
                "userId='" + userId + '\'' +
                ", userNickname='" + userNickname + '\'' +
                ", userEmail='" + userEmail + '\'' +
                ", userName='" + userName + '\'' +
                ", profileImageUrl='" + profileImageUrl + '\'' +
                ", createAt=" + createAt +
                ", modifiedAt='" + modifiedAt + '\'' +
                ", householdId=" + householdId +
                '}';
    }
}
