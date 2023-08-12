package com.mirror.backend.api.entity;

import com.mirror.backend.api.dto.MessageDto;
import lombok.*;
import javax.persistence.*;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import java.time.LocalDateTime;


@Entity
@Getter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class VideoMessage {


    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long videoId;

    private String userEmail;
    private String sendUserEmail;
    private String type;
    private LocalDateTime date;
    private Character isRead;

    @Builder
    public VideoMessage(MessageDto.RequestMessage requestMessage, LocalDateTime date) {
        this.userEmail = requestMessage.getSendUserEmail();
        this.sendUserEmail = requestMessage.getUserEmail();
        this.type = requestMessage.getType();
        this.date = date;
        this.isRead = 'N';
    }

    public void update(Character isRead) {
        this.isRead = isRead;
    }
}
