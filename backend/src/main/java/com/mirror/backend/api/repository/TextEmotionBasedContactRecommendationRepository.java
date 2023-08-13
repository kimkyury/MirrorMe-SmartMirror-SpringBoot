package com.mirror.backend.api.repository;

import com.mirror.backend.api.entity.TextEmotionBasedContactRecommendation;
import com.mirror.backend.api.entity.TextSummarySchedule;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TextEmotionBasedContactRecommendationRepository extends CrudRepository<TextEmotionBasedContactRecommendation, String> {

}
