package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.Interest;
import com.mirror.backend.api.entity.Mirror;
import com.mirror.backend.api.entity.keys.InterestKey;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface MirrorRepository extends JpaRepository<Mirror, String> {
    Optional<Mirror> findByMirrorId (String mirrorId);
}
