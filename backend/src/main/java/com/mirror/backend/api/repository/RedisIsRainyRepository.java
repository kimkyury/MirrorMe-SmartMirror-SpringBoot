package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.TextCautionRainy;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RedisIsRainyRepository extends CrudRepository<TextCautionRainy, String> {

}
