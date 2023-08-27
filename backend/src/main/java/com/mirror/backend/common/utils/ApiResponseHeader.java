package com.mirror.backend.common.utils;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import lombok.AllArgsConstructor;

@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class ApiResponseHeader {
    private int code;
    private String message;
}