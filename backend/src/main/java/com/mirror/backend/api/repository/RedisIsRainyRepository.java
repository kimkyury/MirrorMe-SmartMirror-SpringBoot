package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.RedisFamilyBirthday;
import com.mirror.backend.api.entity.RedisIsRainy;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RedisIsRainyRepository extends CrudRepository<RedisIsRainy, String> {

}
