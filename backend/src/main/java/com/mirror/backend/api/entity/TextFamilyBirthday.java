package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@RedisHash("familyBirth")
public class TextFamilyBirthday {

    @Id
    private String userEmail;
    private String familyBirthday;
    private String targetDay;

    @Builder
    public TextFamilyBirthday(String userEmail, String familyBirthday, String targetDay) {
        this.userEmail = userEmail;
        this.familyBirthday = familyBirthday;
        this.targetDay = targetDay;
    }
}
