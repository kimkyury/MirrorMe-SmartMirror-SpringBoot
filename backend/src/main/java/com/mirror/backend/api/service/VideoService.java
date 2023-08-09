package com.mirror.backend.api.service;

import com.mirror.backend.api.entity.VideoMessage;
import org.springframework.web.multipart.MultipartFile;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.List;

public interface VideoService {
    int matchVideo(String text);
    List<VideoMessage> getVideo(String userEmail);
    FileInputStream getVideoDetail(Long videoId) throws FileNotFoundException;
    String transferFile(MultipartFile videoFile, String filePath);
}
