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
    private Long householdId;

    @ManyToOne
    @JoinColumn(name = "createUserId")
    private User createUser;

    private String householdName;

    private int gridNx;

    private int gridNy;

    private String region;

    @Builder
    public Household(Long householdId, User createUser, String householdName, int gridNx, int gridNy, String region) {
        this.householdId = householdId;
        this.createUser = createUser;
        this.householdName = householdName;
        this.gridNx = gridNx;
        this.gridNy = gridNy;
        this.region = region;
    }

    @Override
    public String toString() {
        return "Household{" +
                "householdId=" + householdId +
                ", createUserId=" + createUser.getUserId() +
                ", householdName='" + householdName + '\'' +
                ", gridNx=" + gridNx +
                ", gridNy=" + gridNy +
                ", region='" + region + '\'' +
                '}';
    }
}