package com.mirror.backend.api.entity;

import com.mirror.backend.api.entity.keys.ConnectUserKey;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.domain.Persistable;

import javax.persistence.*;
import java.time.LocalDate;

@Entity
@Getter
@Setter
@Table(name = "connect_users")
@NoArgsConstructor
public class ConnectUser  {

    @EmbeddedId
    private ConnectUserKey id;

    @ManyToOne
    @MapsId("userId")  // ConnectUserKey의 userId 필드와 매핑
    @JoinColumn(name = "userId")  // 실제 DB 테이블의 컬럼 이름
    private User user;

    @ManyToOne
    @MapsId("connectUserId")  // ConnectUserKey의 connectUserId 필드와 매핑
    @JoinColumn(name = "connectUserId")  // 실제 DB 테이블의 컬럼 이름
    private User connectUser;

    private String connectUserAlias;

    @Builder
    public ConnectUser(ConnectUserKey id, User user, User connectUser, String connectUserAlias) {
        this.id = id;
        this.user = user;
        this.connectUser = connectUser;
        this.connectUserAlias = connectUserAlias;
    }

    @Override
    public String toString() {
        return "ConnectUser{" +
                "userId=" + id.getUserId() +
                ", connectUserId='" + id.getConnectUserId() + '\'' +
                ", userAlias='" + connectUserAlias + '\'' +
                '}';
    }
}
