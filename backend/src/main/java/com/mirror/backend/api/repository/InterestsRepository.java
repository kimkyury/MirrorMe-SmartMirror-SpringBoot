package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.Interest;
import com.mirror.backend.api.entity.keys.InterestKey;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface InterestsRepository extends JpaRepository<Interest, InterestKey> {
    Optional<Interest> findByIdUserIdAndIdInterestCode(Long userId, Long interestCode);
    List<Interest> findByIdUserIdAndIsUsed(Long userId, int isUsed);
}
