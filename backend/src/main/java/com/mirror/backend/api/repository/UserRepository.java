package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUserName(String userName);

    Optional<User> findByUserEmail(String userEmail);

    Optional<User> findByUserId(Long userId);


}
