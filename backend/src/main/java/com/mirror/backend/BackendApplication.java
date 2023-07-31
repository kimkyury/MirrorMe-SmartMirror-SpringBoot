package com.mirror.backend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;

import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;

@EnableScheduling
@SpringBootApplication
public class BackendApplication {

    public static void main(String[] args) {
        SpringApplication.run(BackendApplication.class, args);
    }

    @Scheduled(cron = "0 * * * * *")
    public void run() {
        Date now = new Date();

        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyyMMddHHmm");
        System.out.println("simpleDateFormat = " + simpleDateFormat.format(now));

        String folderPath = "/home/ubuntu/message/" + simpleDateFormat.format(now);

    }
}
