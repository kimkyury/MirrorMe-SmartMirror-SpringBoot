package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class RequestInterestDto {

    @JsonProperty("interestCode")
    Long interestCode;

    @Override
    public String toString() {
        return "RequestInterestDto{" +
                "interestCode=" + interestCode +
                '}';
    }
}
