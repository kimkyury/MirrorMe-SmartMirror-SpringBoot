package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.Interests;
import com.mirror.backend.api.entity.keys.InterestKey;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface InterestsRepository extends JpaRepository<Interests, InterestKey> {
    Optional<Interests> findByIdUserIdAndIdInterestCode(Long userId, Long interestCode);

}
