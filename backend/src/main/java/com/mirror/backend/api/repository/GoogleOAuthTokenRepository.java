package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.GoogleOAuthToken;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface GoogleOAuthTokenRepository extends CrudRepository<GoogleOAuthToken, String> {

}
