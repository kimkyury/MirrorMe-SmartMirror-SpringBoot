package com.mirror.backend.api.entity;


import com.fasterxml.jackson.annotation.JsonProperty;
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
    String mirror_id;
    @JsonProperty("mirrorGroupId")
    String mirror_group_id;
    @JsonProperty("mirrorPlaceCode")
    String mirror_place_code;

    @Override
    public String toString() {
        return "Mirror{" +
                "mirror_id='" + mirror_id + '\'' +
                ", mirror_group_id='" + mirror_group_id + '\'' +
                '}';
    }

}
