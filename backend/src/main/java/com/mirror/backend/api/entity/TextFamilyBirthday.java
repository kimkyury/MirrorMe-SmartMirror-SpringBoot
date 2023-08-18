package com.mirror.backend.api.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@RedisHash("textFamilyBirthday")
public class TextFamilyBirthday {

    @Id
    private String userEmail;
    private String textFamilyBirthday;
    private String targetDay;

    @Builder
    public TextFamilyBirthday(String userEmail, String textFamilyBirthday, String targetDay) {
        this.userEmail = userEmail;
        this.textFamilyBirthday = textFamilyBirthday;
        this.targetDay = targetDay;
    }
}
