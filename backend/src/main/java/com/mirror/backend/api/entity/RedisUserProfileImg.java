package com.mirror.backend.api.entity;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@Getter
@Setter
@Builder
@RedisHash("profileImg")
public class RedisUserProfileImg {

    @Id
    private String userEmail;
    private byte[] profileImg;


    public RedisUserProfileImg(String userEmail, byte[] profileImg ) {
        this.userEmail = userEmail;
        this.profileImg = profileImg;
    }
}
