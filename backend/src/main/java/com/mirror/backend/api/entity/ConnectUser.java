package com.mirror.backend.api.entity;

import com.mirror.backend.api.entity.keys.ConnectUserKey;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Getter
@Setter
@Table(name = "connect_users")
@NoArgsConstructor
public class ConnectUser {

    @EmbeddedId
    private ConnectUserKey id;
    private String connectUserAlias;

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
