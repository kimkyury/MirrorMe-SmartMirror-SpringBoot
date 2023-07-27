package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.Message;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

public interface VideoService {
    int matchVideo(String text);
    int saveVideo(String videoPath, String voicePath);
    List<Message.ResponseMessage> getVideo(int userId);
    String transferFile(MultipartFile videoFile, String filePath);
}
