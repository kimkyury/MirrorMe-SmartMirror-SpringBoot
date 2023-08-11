package com.mirror.backend.common.handler;

import com.mirror.backend.common.utils.ApiUtils;
import org.springframework.http.HttpStatus;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.NoHandlerFoundException;
import org.webjars.NotFoundException;

import javax.validation.ConstraintViolationException;
import static com.mirror.backend.common.utils.ApiUtils.error;


@ControllerAdvice
public class GlobalExceptionHandler {
    private final Logger logger = LoggerFactory.getLogger(getClass());

    @ExceptionHandler({
            IllegalArgumentException.class,
            IllegalStateException.class,
            ConstraintViolationException.class,
            MethodArgumentNotValidException.class,
    })
    public ApiUtils.ApiResult<?> handleBadRequestException(Exception e) {
        logger.debug("Bad request exception occurred: {}", e.getMessage(), e);
        if (e instanceof MethodArgumentNotValidException) {
            return error(
                    ((MethodArgumentNotValidException) e).getBindingResult().getAllErrors().get(0).getDefaultMessage(),
                    HttpStatus.BAD_REQUEST
            );
        }
        return error(e, HttpStatus.BAD_REQUEST);
    }


    @ExceptionHandler({
            NoHandlerFoundException.class,
            NotFoundException.class,
    })
    public ApiUtils.ApiResult<?> handleNotFoundException(Exception e) {
        return error(e, HttpStatus.NOT_FOUND);
    }
}
