package com.mirror.backend.api.entity;

import com.mirror.backend.api.entity.keys.ConnectUserKey;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter
@Setter
@Table(name = "connect_users")
@NoArgsConstructor
public class ConnectUser {

    @EmbeddedId
    private ConnectUserKey id;
    private String connectUserAlias;

    @ManyToOne
    @MapsId("userId")  // ConnectUserKey의 userId 필드와 매핑
    @JoinColumn(name = "userId")  // 실제 DB 테이블의 컬럼 이름
    private User user;

    @ManyToOne
    @MapsId("connectUserId")  // ConnectUserKey의 connectUserId 필드와 매핑
    @JoinColumn(name = "connectUserId")  // 실제 DB 테이블의 컬럼 이름
    private User connectUser;

    @Builder
    public ConnectUser(ConnectUserKey id, String connectUserAlias) {
        this.id = id;
        this.connectUserAlias = connectUserAlias;
    }

    @Override
    public String toString() {
        return "ConnectUser{" +
                "id=" + id +
                ", userAlias='" + connectUserAlias + '\'' +
                '}';
    }
}
