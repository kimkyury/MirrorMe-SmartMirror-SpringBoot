package com.mirror.backend.api.repository;

import com.mirror.backend.api.dto.chatbotDtos.ResponseFirstMirrorTextDto;
import com.mirror.backend.api.entity.RedisMirrorFirstText;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RedisFirstMirrorTextRepository extends CrudRepository<RedisMirrorFirstText, String> {

}
