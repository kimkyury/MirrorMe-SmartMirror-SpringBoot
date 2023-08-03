package com.mirror.backend.api.dto;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

// from ConnectUser 테이블에서 일부만 사용하는 Dto
@Setter
@Getter
public class Alias {

    private String connectUserEmail;
    private String connectUserAlias;

    @Builder
    public Alias(String connectUserEmail, String connectUserAlias) {
        this.connectUserEmail = connectUserEmail;
        this.connectUserAlias = connectUserAlias;
    }

    @Override
    public String toString() {
        return "Alias{" +
                connectUserEmail + "="
                + connectUserAlias + '\'' +
                '}';
    }
}
