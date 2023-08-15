package com.mirror.backend.api.scheduler;

import com.mirror.backend.api.entity.Emotion;
import com.mirror.backend.api.entity.EmotionCount;
import com.mirror.backend.api.repository.EmotionCountRepository;
import com.mirror.backend.api.repository.EmotionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.util.List;

@Component
public class EmotionSaveScheduler {

    @Autowired
    private EmotionRepository emotionRepository;

    @Autowired
    private EmotionCountRepository emotionCountRepository;

    @Scheduled(cron = "0 0 0 * * *")
    public void emotionSave() {
        LocalDate oneDayAgo = LocalDate.now().minusDays(1);
        List<Emotion> emotionList = emotionRepository.findAllByEmotionDate(oneDayAgo);
        for(int i=0; i<emotionList.size(); i++) {
            Emotion emotion = emotionList.get(i);

            List<EmotionCount> emotionCountList = emotionCountRepository.findAllByEmotionKeyEmotionId(emotion.getEmotionId());

            int max = 0, idx = 0;
            for(EmotionCount emotionCount : emotionCountList) {
                if(max < emotionCount.getEmotionCount()) {
                    max = emotionCount.getEmotionCount();
                    idx = emotionCount.getEmotionKey().getEmotionCode();
                }
            }

            emotion.update(idx);
            emotionRepository.save(emotion);
        }
    }
}
