package com.mirror.backend.common.exception;

public class FailConvertException extends RuntimeException {

    public FailConvertException(String message) {
        super(message);
    }

    public FailConvertException(String message, Throwable cause) {
        super(message, cause);
    }
}