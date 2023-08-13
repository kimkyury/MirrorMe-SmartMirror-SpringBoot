package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.TextFamilyBirthday;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TextFamilyBirthdayRepository extends CrudRepository<TextFamilyBirthday, String> {

}
