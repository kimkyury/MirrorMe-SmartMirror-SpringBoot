package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.TextSummarySchedule;
import com.mirror.backend.api.entity.TextVideoView;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TextVideoViewRepository extends CrudRepository<TextVideoView, String> {

}
