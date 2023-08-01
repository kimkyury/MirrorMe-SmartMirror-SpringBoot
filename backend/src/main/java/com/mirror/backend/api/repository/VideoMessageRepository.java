package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.VideoMessage;
import org.springframework.data.repository.CrudRepository;

public interface VideoMessageRepository extends CrudRepository<VideoMessage, Integer> {
}
