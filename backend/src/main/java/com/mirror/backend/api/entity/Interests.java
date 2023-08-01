package com.mirror.backend.api.entity;

import com.mirror.backend.api.entity.keys.InterestKey;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Getter
@Setter
@Table(name = "interests")
public class Interests {

    @EmbeddedId
    private InterestKey id;

    private int isUsed; // 0:사용 아님, 1: 사용 중임

    @Override
    public String toString() {
        return "Interests{" +
                "id=" + id +
                ", isUsed=" + isUsed +
                '}';
    }
}
