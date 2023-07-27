package com.mirror.backend.api.service.impl;

import org.apache.commons.io.IOUtils;
import org.apache.tomcat.util.codec.binary.Base64;
import com.mirror.backend.api.dto.Message;
import com.mirror.backend.api.entity.VideoMessage;
import com.mirror.backend.api.repository.VideoMessageRepository;
import com.mirror.backend.api.service.VideoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class VideoServiceImpl implements VideoService {

    @Autowired
    private VideoMessageRepository videoMessageRepository;

    @Override
    public int matchVideo(String text) {
        System.out.println("text = " + text);
        if(text.contains("영상") || text.contains("비디오")) {
            return 1;
        }
        return 0;
    }

    @Override
    public int saveVideo(String videoPath, String voicePath) {
        VideoMessage message = new VideoMessage(1, 2, videoPath, voicePath);
        return videoMessageRepository.save(message).getUserId();
    }

    @Override
    public List<Message.ResponseMessage> getVideo(int userId) {
        Optional<VideoMessage> videoList = videoMessageRepository.findById(userId);
        if(!videoList.isPresent()) return null;
        List<VideoMessage> videoMessageList = videoList.stream().collect(Collectors.toList());

        List<Message.ResponseMessage> responseMessages = new ArrayList<>();
        for(VideoMessage videoMessage : videoMessageList) {
            String videoPath = videoMessage.getVideoPath();
            String voicePath = videoMessage.getVoicePath();

            try {
                InputStream inputStream = new FileInputStream(videoPath);
                byte[] images = IOUtils.toByteArray(inputStream);
                byte[] byteEnc64 = Base64.encodeBase64(images);
                String imgStr = new String(byteEnc64, "UTF-8");

                inputStream.close();
            } catch (IOException e) {
                e.printStackTrace();
            }


        }

        return responseMessages;
    }

    @Override
    public String transferFile(MultipartFile videoFile, String filePath) {
        String originalFilename = videoFile.getOriginalFilename();
        String fileName = originalFilename.substring(originalFilename.lastIndexOf("\\") + 1);
        String uuid = UUID.randomUUID().toString();

        String saveFileName = filePath + File.separator + uuid + "_" + fileName;
        Path savePath = Paths.get(saveFileName);

        try {
            videoFile.transferTo(savePath);
            return saveFileName;
        }catch (IOException e) {
            e.printStackTrace();
        }

        return null;
    }
}
