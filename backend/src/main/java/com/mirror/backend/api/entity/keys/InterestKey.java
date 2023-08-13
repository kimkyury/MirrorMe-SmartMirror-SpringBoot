package com.mirror.backend.api.entity.keys;


import lombok.*;

import javax.persistence.Embeddable;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.MapsId;
import java.io.Serializable;

@Getter
@Embeddable
@NoArgsConstructor
@EqualsAndHashCode
public class InterestKey implements Serializable {

    private Long userId;
    private Long interestCode;

    public InterestKey(Long userId, Long interestCode) {
        this.userId = userId;
        this.interestCode = interestCode;
    }
}
