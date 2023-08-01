package com.mirror.backend.api.entity.keys;


import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Embeddable;
import java.io.Serializable;

@Getter
@Setter
@Embeddable
@NoArgsConstructor
public class InterestKey implements Serializable {

    private Long userId;
    private Long interestCode;



    public InterestKey(Long userId, Long interestCode) {
        this.userId = userId;
        this.interestCode = interestCode;
    }
}
