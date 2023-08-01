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
public class ConnectUserKey implements Serializable {

    private Long userId;
    private Long connectUserId;

    public ConnectUserKey(Long userId, Long connectUserId) {
        this.userId = userId;
        this.connectUserId = connectUserId;
    }

}
