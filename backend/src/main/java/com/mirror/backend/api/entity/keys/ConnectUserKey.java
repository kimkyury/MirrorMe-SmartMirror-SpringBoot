package com.mirror.backend.api.entity.keys;

import lombok.*;

import javax.persistence.Embeddable;
import java.io.Serializable;

@Getter
@Embeddable
@NoArgsConstructor
@EqualsAndHashCode
public class ConnectUserKey implements Serializable {

    private Long userId;
    private Long connectUserId;

    public ConnectUserKey(Long userId, Long connectUserId) {
        this.userId = userId;
        this.connectUserId = connectUserId;
    }
}
