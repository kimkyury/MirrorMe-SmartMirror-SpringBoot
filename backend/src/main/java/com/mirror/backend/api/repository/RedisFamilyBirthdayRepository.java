package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.RedisFamilyBirthday;
import com.mirror.backend.api.entity.RedisSummeryCalendar;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RedisFamilyBirthdayRepository extends CrudRepository<RedisFamilyBirthday, String> {

}