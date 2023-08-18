package com.mirror.backend.common.utils;

import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Date;


public class EtcUtil {

    public static String getTodayYYYYMMDD(){
        LocalDate today = LocalDate.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd");
        String formattedDate = today.format(formatter);
        return formattedDate;
    }

    public static String getTodayMMDD(){
        LocalDate today = LocalDate.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMdd");
        String formattedDte = today.format(formatter);
        return formattedDte;
    }
}
