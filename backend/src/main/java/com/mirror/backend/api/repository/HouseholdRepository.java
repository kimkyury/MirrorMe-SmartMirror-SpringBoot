package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.Household;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface HouseholdRepository extends JpaRepository<Household, Long> {

    Optional<Household> findByCreateUserId(Long createUserId);

}
