package com.mirror.backend.api.service;

import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.entity.VideoMessage;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

public interface VideoService {
    int matchVideo(String text);
    List<VideoMessage> getVideo(String userEmail);
    Message.ResponseMessageDetail getVideoDetail(Long videoId);
    String transferFile(MultipartFile videoFile, String filePath);
}
