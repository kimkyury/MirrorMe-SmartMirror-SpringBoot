package com.mirror.backend.api.dto;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RedisTestRepository extends CrudRepository<RedisTest, String> {
}
