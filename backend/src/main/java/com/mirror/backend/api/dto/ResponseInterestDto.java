package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@JsonIgnoreProperties(ignoreUnknown = true)
public class ResponseInterestDto {

    @JsonProperty("interestCode")
    private Long interestCode;
    @JsonProperty("interestName")
    private String interestName;

    public ResponseInterestDto(Long interestCode, String interestName) {
        this.interestCode = interestCode;
        this.interestName = interestName;
    }

    @Override
    public String toString() {
        return "ResponseInterestDto{" +
                "interestCode=" + interestCode +
                ", interestName='" + interestName + '\'' +
                '}';
    }
}
