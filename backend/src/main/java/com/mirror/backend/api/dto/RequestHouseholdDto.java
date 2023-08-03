package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class RequestHouseholdDto {

    @JsonProperty("householdName")
    String householdName;

    @Override
    public String toString() {
        return "RequestHouseholdDto{" +
                "householdName='" + householdName + '\'' +
                '}';
    }
}
