package com.mirror.backend.api.repository;

import com.mirror.backend.api.dto.RedisTest;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RedisTestRepository extends CrudRepository<RedisTest, String> {
}
