package com.mirror.backend.common.utils;

import lombok.Getter;
import lombok.Setter;

public class ApiUtils {
    public static <T> ApiResult<T> success(T response) {
        return new ApiResult<>(true, response, null);
    }

    public static <T> ApiResult<T> fail(T response) {
        return new ApiResult<>(false, response, null);
    }

    public static ApiResult<?> error(String message, int status) {
        return new ApiResult<>(false, null, new ApiError(message, status));
    }

    @Getter
    @Setter
    public static class ApiError {
        private final String message;
        private final int status;

        public ApiError(String message, int status) {
            this.message = message;
            this.status = status;
        }
    }

    @Getter
    @Setter
    public static class ApiResult<T> {
        private final boolean success;
        private final T response;
        private final ApiError error;

        private ApiResult(boolean success, T response, ApiError error) {
            this.success = success;
            this.response = response;
            this.error = error;
        }
    }
}
