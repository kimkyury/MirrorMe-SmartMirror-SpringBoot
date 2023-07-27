package com.mirror.backend.api.service;

import org.springframework.web.multipart.MultipartFile;

public interface VideoService {
    int matchVideo(String text);
    int saveVideo(String videoPath, String voicePath);
    String transferFile(MultipartFile videoFile, String filePath);
}
