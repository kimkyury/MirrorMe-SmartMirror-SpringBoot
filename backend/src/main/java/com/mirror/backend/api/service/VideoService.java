package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.Message;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

public interface VideoService {
    int matchVideo(String text);
    void saveVideo(String videoPath, String voicePath, Message.RequestMessage requestMessage);
    List<Message.ResponseMessage> getVideo(int userId);
    String transferFile(MultipartFile videoFile, String filePath);
}
