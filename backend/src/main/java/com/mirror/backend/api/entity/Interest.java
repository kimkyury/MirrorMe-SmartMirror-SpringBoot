package com.mirror.backend.api.entity;

import com.mirror.backend.api.entity.keys.InterestKey;
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
@Table(name = "interests")
@NoArgsConstructor
public class Interest {

    @EmbeddedId
    private InterestKey id;

    private int isUsed; // 0:사용 아님, 1: 사용 중임

    @Builder
    public Interest(InterestKey id, int isUsed) {
        this.id = id;
        this.isUsed = isUsed;
    }

    @Override
    public String toString() {
        return "Interests{" +
                "id=" + id +
                ", isUsed=" + isUsed +
                '}';
    }
}
