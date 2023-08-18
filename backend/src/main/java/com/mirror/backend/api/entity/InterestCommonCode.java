package com.mirror.backend.api.entity;


import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Getter
@Setter
@Table(name = "interest_common_code")
public class InterestCommonCode {

    @Id
    @JsonProperty("interestCode")
    Long interestCode;
    @JsonProperty("interestName")
    String interestName;

    @Override
    public String toString() {
        return "InterestCommonCode{" +
                "interestCode=" + interestCode +
                ", interestName=" + interestName +
                '}';
    }
}
