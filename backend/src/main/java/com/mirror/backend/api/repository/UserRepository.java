package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUserName(String userName);

    User findByUserEmail(String userEmail);

    User findByUserId(Long userId);
}
