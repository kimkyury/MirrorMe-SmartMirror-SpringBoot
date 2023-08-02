package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.RedisUserProfileImg;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RedisUserProfileImgRepository extends CrudRepository<RedisUserProfileImg, String> {

}
