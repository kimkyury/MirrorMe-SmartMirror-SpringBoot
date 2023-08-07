package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.VideoMessage;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface VideoRepository extends JpaRepository<VideoMessage, Long> {
    List<VideoMessage> findAllByUserEmail(String userEmail);
    VideoMessage findByVideoId(Long videoId);
}
