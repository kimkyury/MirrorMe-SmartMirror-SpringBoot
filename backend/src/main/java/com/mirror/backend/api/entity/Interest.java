package com.mirror.backend.api.entity;

import com.mirror.backend.api.entity.keys.InterestKey;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter
@Setter
@Table(name = "interests")
@NoArgsConstructor
public class Interest {

    @EmbeddedId
    private InterestKey id;

    @ManyToOne
    @MapsId("userId")
    @JoinColumn(name = "userId")
    private User user;

    @ManyToOne
    @MapsId("interestCode")
    @JoinColumn(name = "interestCode")
    private InterestCommonCode interestCode;

    private int isUsed; // 0:사용 아님, 1: 사용 중임

    @Builder
    public Interest(InterestKey id, User user, InterestCommonCode interestCode, int isUsed) {
        this.id = id;
        this.user = user;
        this.interestCode = interestCode;
        this.isUsed = isUsed;
    }

    @Override
    public String toString() {
        return "Interest{" +
                "userId=" + id.getUserId() +
                ", interestCode=" + id.getInterestCode() +
                ", isUsed=" + isUsed +
                '}';
    }
}
