package com.mirror.backend.api.entity;


import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Getter
@Setter
@Table(name = "mirrors")
@NoArgsConstructor
public class Mirror {

    @Id
    @JsonProperty("mirrorId")
    String mirrorId;
    @JsonProperty("mirrorGroupId")
    Long mirrorGroupId;
    @JsonProperty("mirrorPlaceCode")
    Long mirrorPlaceCode;

    @Builder
    public Mirror(String mirrorId, Long mirrorGroupId, Long mirrorPlaceCode) {
        this.mirrorId = mirrorId;
        this.mirrorGroupId = mirrorGroupId;
        this.mirrorPlaceCode = mirrorPlaceCode;
    }

    @Override
    public String toString() {
        return "Mirror{" +
                "mirrorId='" + mirrorId + '\'' +
                ", mirrorGroupId='" + mirrorGroupId + '\'' +
                ", mirrorPlaceCode='" + mirrorPlaceCode + '\'' +
                '}';
    }
}
