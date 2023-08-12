package com.mirror.backend.common.utils;

import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Date;


public class EtcUtil {

    public static String getTodayYYYYMMDD(){
        LocalDate today = LocalDate.now();  // 오늘의 날짜 가져오기
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd");  // 원하는 날짜 형식 정의
        String formattedDate = today.format(formatter);  // 날짜를 원하는 형식으로 변환
        return formattedDate;
    }

    public static String getTodayMMDD(){
        LocalDate today = LocalDate.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMdd");
        String formattedDte = today.format(formatter);
        return formattedDte;
    }
}
