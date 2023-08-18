package com.mirror.backend.common.utils;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

import java.util.HashMap;
import java.util.Map;

@Getter
@RequiredArgsConstructor
public class ApiResponse<T> {

    private final static int SUCCESS = 200;
    private final static int BAD_REQUEST = 400;
    private final static int FORBIDDEN = 403;
    private final static int NOT_FOUND = 404;
    private final static int FAILED = 500;

    private final static String SUCCESS_MESSAGE = "SUCCESS";
    private final static String BAD_REQUEST_MESSAGE = "잘못된 요청입니다.";
    private final static String FORBIDDEN_MESSAGE = "요청 권한이 없습니다.";
    private final static String NOT_FOUND_MESSAGE = "데이터를 찾을 수 없습니다.";
    private final static String FAILED_MESSAGE = "서버에서 오류가 발생하였습니다.";


    private final static String INVALID_ACCESS_TOKEN = "Invalid access token.";
    private final static String INVALID_REFRESH_TOKEN = "Invalid refresh token.";
    private final static String INVALID_USER_ID = "Invalid user id.";
    private final static String INVALID_USER_EMAIL = "Invalid user email.";
    private final static String NOT_EXPIRED_TOKEN_YET = "Not expired token yet.";

    //Custom Error Message (KIMKYURI)
    private final static String NOT_FOUNT_MIRROR_MESSAGE = "등록되지 않은 미러입니다.";


    private final ApiResponseHeader header;
    private final Map<String, T> body;

    public static <T> ApiResponse<T> success(String name, T body) {
        Map<String, T> map = new HashMap<>();
        map.put(name, body);

        return new ApiResponse(new ApiResponseHeader(SUCCESS, SUCCESS_MESSAGE), map);
    }

    public static <T> ApiResponse<T> fail() {
        return new ApiResponse(new ApiResponseHeader(FAILED, FAILED_MESSAGE), null);
    }

    public static <T> ApiResponse<T> invalidAccessToken() {
        return new ApiResponse(new ApiResponseHeader(FAILED, INVALID_ACCESS_TOKEN), null);
    }

    public static <T> ApiResponse<T> invalidRefreshToken() {
        return new ApiResponse(new ApiResponseHeader(FAILED, INVALID_REFRESH_TOKEN), null);
    }

    public static <T> ApiResponse<T> notExpiredTokenYet() {
        return new ApiResponse(new ApiResponseHeader(FAILED, NOT_EXPIRED_TOKEN_YET), null);
    }

    // Additional Message
    public static <T> ApiResponse<T> badRequest() {
        return new ApiResponse(new ApiResponseHeader(BAD_REQUEST, BAD_REQUEST_MESSAGE), null);
    }
    public static <T> ApiResponse<T> forbidden() {
        return new ApiResponse(new ApiResponseHeader(FORBIDDEN, FORBIDDEN_MESSAGE), null);
    }
    public static <T> ApiResponse<T> notFound() {
        return new ApiResponse(new ApiResponseHeader(NOT_FOUND, NOT_FOUND_MESSAGE), null);
    }


    // Mirror Error
    public static <T> ApiResponse<T> notFountMirror() {
        return new ApiResponse(new ApiResponseHeader(NOT_FOUND, NOT_FOUNT_MIRROR_MESSAGE), null);
    }

}
