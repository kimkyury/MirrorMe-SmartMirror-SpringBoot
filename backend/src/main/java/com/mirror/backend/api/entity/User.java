package com.mirror.backend.api.entity;

import com.fasterxml.jackson.annotation.JsonManagedReference;
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

    private String userEmail;

    private String userName;

    private String password;

    private LocalDateTime createAt;

    private LocalDateTime modifiedAt;

    @ManyToOne
    @JoinColumn(name = "householdId")
    @JsonManagedReference   // 순환참조 방지 - 부모
    private Household household;

    private String birthday;

    @Builder
    public User(Long userId, String userEmail, String userName, String password, LocalDateTime createAt, LocalDateTime modifiedAt, Household household, String birthday) {
        this.userId = userId;
        this.userEmail = userEmail;
        this.userName = userName;
        this.password = password;
        this.createAt = createAt;
        this.modifiedAt = modifiedAt;
        this.household = household;
        this.birthday = birthday;
    }

    @Override
    public String toString() {
        return "User{" +
                "userId=" + userId +
                ", userEmail='" + userEmail + '\'' +
                ", userName='" + userName + '\'' +
                ", password='" + password + '\'' +
                ", createAt=" + createAt +
                ", modifiedAt=" + modifiedAt +
                ", household=" + household.householdId +
                ", birthDay='" + birthday + '\'' +
                '}';
    }
}
