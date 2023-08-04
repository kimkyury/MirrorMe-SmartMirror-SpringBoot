package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.Message;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

public interface VideoService {
    int matchVideo(String text);
    List<Message.ResponseMessage> getVideo(String userEmail);
    Message.ResponseMessage getOneVideo(int index, String userEmail);
    String transferFile(MultipartFile videoFile, String filePath);
}
