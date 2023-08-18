package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.ConnectUser;
import com.mirror.backend.api.entity.keys.ConnectUserKey;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;


public interface ConnectUserRepository extends JpaRepository<ConnectUser, ConnectUserKey> {
    Optional<ConnectUser> findByIdUserIdAndIdConnectUserId(Long userId, Long connectUserId);
    List<ConnectUser> findByIdUserId(Long userId);
    Optional<ConnectUser> findByIdUserIdAndConnectUserAlias(Long userId, String userAlias);

}
