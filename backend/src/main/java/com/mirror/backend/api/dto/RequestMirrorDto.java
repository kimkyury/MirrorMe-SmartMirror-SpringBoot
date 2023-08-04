package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class RequestMirrorDto {

    @JsonProperty("mirrorId")
    String mirrorId;

    @JsonProperty("mirrorPlaceCode")
    Long mirrorPlaceCode;

    @Override
    public String toString() {
        return "RequestMirrorDto{" +
                "mirrorId=" + mirrorId +
                ", mirrorPlaceCode=" + mirrorPlaceCode +
                '}';
    }
}
