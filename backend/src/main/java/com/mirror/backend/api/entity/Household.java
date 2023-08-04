package com.mirror.backend.api.entity;


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
    @JsonProperty("householdId")
    Long householdId;
    @JsonProperty("createUserId")
    Long createUserId;
    @JsonProperty("householdName")
    String householdName;
    @JsonProperty("latitude")
    Double latitude;
    @JsonProperty("longitude")
    Double longitude;
    @JsonProperty("region")
    String region;

    @Builder
    public Household(Long householdId, Long createUserId, String householdName, Double latitude, Double longitude, String region) {
        this.householdId = householdId;
        this.createUserId = createUserId;
        this.householdName = householdName;
        this.latitude = latitude;
        this.longitude = longitude;
        this.region = region;
    }

    @Override
    public String toString() {
        return "Household{" +
                "householdId=" + householdId +
                ", createUserId=" + createUserId +
                ", householdName='" + householdName + '\'' +
                ", latitude=" + latitude +
                ", longitude=" + longitude +
                ", region=" + region +
                '}';
    }
}