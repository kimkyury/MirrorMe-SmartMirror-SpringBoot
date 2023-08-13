package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.TextFamilyBirthday;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RedisFamilyBirthdayRepository extends CrudRepository<TextFamilyBirthday, String> {

}
