package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.Household;
import com.mirror.backend.api.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface HouseholdRepository extends JpaRepository<Household, Long> {

    Optional<Household> findByCreateUserUserId(Long createUserId);
    Optional<Household> findByHouseholdId(Long houseHoldId);
}
