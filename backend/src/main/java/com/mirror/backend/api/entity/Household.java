package com.mirror.backend.api.entity;


import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@Table(name = "households")
public class Household {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    Long householdId;

    @ManyToOne
    @JoinColumn(name = "createUserId")
    @JsonBackReference // 순환참조 방지 - 자식
    User createUserId;

    String householdName;
    int gridNx;
    int gridNy;
    String region;

    @Builder
    public Household(Long householdId, User createUserId, String householdName, int gridNx, int gridNy, String region) {
        this.householdId = householdId;
        this.createUserId = createUserId;
        this.householdName = householdName;
        this.gridNx = gridNx;
        this.gridNy = gridNy;
        this.region = region;
    }

    @Override
    public String toString() {
        return "Household{" +
                "householdId=" + householdId +
                ", createUserId=" + createUserId.getHousehold() +
                ", householdName='" + householdName + '\'' +
                ", gridNx=" + gridNx +
                ", gridNy=" + gridNy +
                ", region='" + region + '\'' +
                '}';
    }
}