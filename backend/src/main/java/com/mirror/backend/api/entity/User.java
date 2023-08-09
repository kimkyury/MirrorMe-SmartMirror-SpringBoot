package com.mirror.backend.api.entity;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@NoArgsConstructor
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;

    @JsonProperty("userEmail")
    private String userEmail;

    @JsonProperty("userName")
    private String userName;

    private String password;

    @JsonProperty("createAt")
    private LocalDateTime createAt;

    @JsonProperty("modifiedAt")
    private LocalDateTime modifiedAt;

    @JsonProperty("householdId")
    private Long householdId;

    @Builder
    public User(Long userId, String userEmail, String userName, String password, LocalDateTime createAt, LocalDateTime modifiedAt, Long householdId) {
        this.userId = userId;
        this.userEmail = userEmail;
        this.userName = userName;
        this.password = password;
        this.createAt = createAt;
        this.modifiedAt = modifiedAt;
        this.householdId = householdId;
    }

    @Override
    public String toString() {
        return "User{" +
                "userId=" + userId +
                ", userEmail='" + userEmail + '\'' +
                ", userName='" + userName + '\'' +
                ", createAt=" + createAt +
                ", modifiedAt=" + modifiedAt +
                ", householdId=" + householdId +
                '}';
    }
}
