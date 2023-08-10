package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUserEmail(String userEmail);

    Optional<User> findByUserId(Long userId);

    List<User> findByHouseholdHouseholdId(Long householdId);

    List<User> findByBirthday(String birthday);

    List<User> findByBirthdayAndUserIdIn(String todayBirthday, List<Long> connectUserIds);

}
