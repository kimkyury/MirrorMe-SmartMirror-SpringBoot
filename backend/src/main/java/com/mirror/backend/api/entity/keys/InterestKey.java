package com.mirror.backend.api.entity.keys;


import lombok.Getter;
import lombok.Setter;

import javax.persistence.Embeddable;
import java.io.Serializable;

@Getter
@Setter
@Embeddable
public class InterestKey implements Serializable {

    private Long userId;
    private Long interestCode;


}
