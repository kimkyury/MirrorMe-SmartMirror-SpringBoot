import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:path_provider/path_provider.dart'; // path_provider 패키지 임포트
import 'package:video_player/video_player.dart';
import 'dart:io';

class Message extends StatefulWidget {
  @override
  _MessageState createState() => _MessageState();
}

class _MessageState extends State<Message> {
  VideoPlayerController? _controller; // Nullable로 변경
  
  @override
  void initState() {
    super.initState();
    // 비디오 URL 설정
    String videoUrl = "http://i9e101.p.ssafy.io:8080/api/iot/message?videoId=10"; // 실제 URL로 변경해야 함

    // 비디오 데이터 다운로드 후 비디오 재생
    _initializeVideoPlayer(videoUrl);
  }

  Future<void> _initializeVideoPlayer(String videoUrl) async {
    // 비디오 데이터 다운로드
    final response = await http.get(Uri.parse(videoUrl));
    final videoData = response.bodyBytes;

    // 임시 디렉토리 얻기
    final tempDir = await getTemporaryDirectory();

    // 임시 파일 생성
    final videoFile = File('${tempDir.path}/tempVideo.mp4');
    await videoFile.writeAsBytes(videoData);

    // VideoPlayerController 초기화 및 재생
    _controller = VideoPlayerController.file(videoFile)
      ..initialize().then((_) {
        setState(() {});
        _controller!.play(); // null 체크 후 접근
      });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Image.asset('lib/assets/MirrorMe_Main.png'),
        backgroundColor: Colors.white,
        centerTitle: true,
      ),
      body: Center(
        child: _controller?.value.isInitialized ?? false
            ? AspectRatio(
                aspectRatio: _controller!.value.aspectRatio,
                child: VideoPlayer(_controller!),
              )
            : CircularProgressIndicator(), // 비디오가 준비되기 전에 로딩 표시
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          if (_controller != null) {
            if (_controller!.value.isPlaying) {
              _controller!.pause();
            } else {
              _controller!.play();
            }
          }
        },
        child: Icon(
          _controller?.value.isPlaying ?? false
              ? Icons.pause
              : Icons.play_arrow,
        ),
      ),
    );
  }

  @override
  void dispose() {
    super.dispose();
    _controller?.dispose(); // null 체크 후 해제
  }
}
