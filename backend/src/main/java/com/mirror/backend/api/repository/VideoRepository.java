package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.VideoMessage;
import io.lettuce.core.dynamic.annotation.Param;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface VideoRepository extends JpaRepository<VideoMessage, Long> {
    List<VideoMessage> findAllByUserEmail(String userEmail);
    Optional<VideoMessage> findByVideoId(Long videoId);
    @Query("SELECT count(e) from VideoMessage e where MONTH(e.date) = :month and e.userEmail = :userEmail")
    Integer findByMonth(@Param("month") int month, @Param("userEmail") String userEmail);
    List<VideoMessage> findAllByIsReadAndUserEmail(Character isRead, String userEmail);
}
