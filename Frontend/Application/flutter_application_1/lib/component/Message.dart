import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:path_provider/path_provider.dart'; // path_provider 패키지 임포트
import 'package:video_player/video_player.dart';
import 'dart:io';
import 'dart:convert';

class Message extends StatelessWidget {

  final String accessToken;
  final String refreshToken;

  Message({required this.accessToken, required this.refreshToken});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Image.asset('lib/assets/MirrorMe_Main.png'),
        backgroundColor: Colors.white,
        centerTitle: true,
        leading: IconButton(
          icon: Image.asset('lib/assets/back.png'), // 원하는 이미지로 대체
          onPressed: () {
            Navigator.of(context).pop(); // 뒤로 가기 기능 실행
          },
        ),
      ),
      body: MessageListView(
        accessToken: accessToken,
        refreshToken: refreshToken,
      ),
    );
  }
}

class MessageListView extends StatefulWidget {
    final String accessToken;
    final String refreshToken;

    MessageListView({required this.accessToken, required this.refreshToken});

  @override
  _MessageListViewState createState() => _MessageListViewState();
}

class _MessageListViewState extends State<MessageListView> {
  List<Map<String, dynamic>> messages = []; // 메시지 리스트 초기화

  @override
  void initState() {
    super.initState();
    _fetchData(); // 페이지가 로드될 때 초기 데이터를 불러오기 위해 _fetchData 호출
  }

  Future<void> _fetchData() async {
    final url = 'http://i9e101.p.ssafy.io:8080/video'; 
    

    var headers = {
      'access_token': widget.accessToken, // access_token 추가
    };

    var cookies = {
      'refresh_token': widget.refreshToken, // refresh_token을 쿠키에 추가
    };

    try {
      final response = await http.get(
        Uri.parse(url),
        headers: headers,
        // cookie: cookies,
      );

      if (response.statusCode == 200) {
        final responseData = json.decode(response.body);
        final newMessages = List<Map<String, dynamic>>.from(responseData['response']);

        setState(() {
          messages = newMessages; // 메시지 리스트 업데이트
        });

        print('Response Data: ${response.body}');
      } else if (response.statusCode == 401) {
        print(401);
        print('Response Data: ${response.body}');
      }
      else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error during HTTP request: $e');
    }
  }

  void _playVideo(int videoId, String sendUserEmail) async {
    final videoUrl = 'http://i9e101.p.ssafy.io:8080/api/iot/message?videoId=$videoId';

    try {
      // 비디오 데이터 다운로드 후 비디오 재생
      final response = await http.get(Uri.parse(videoUrl));
      final videoData = response.bodyBytes;

      final tempDir = await getTemporaryDirectory();

      final videoFile = File('${tempDir.path}/tempVideo.mp4');
      await videoFile.writeAsBytes(videoData);

      final VideoPlayerController controller = VideoPlayerController.file(videoFile);
      await controller.initialize();

      // 모달 형태로 동영상 재생 화면 표시
      showModalBottomSheet(
          context: context,
          backgroundColor: Colors.black.withOpacity(0.7), // 반투명 검은 배경
          isScrollControlled: true, // 모달이 가운데에 나오도록 설정
          builder: (context) {
            return Center(
              child: Container(
                height: MediaQuery.of(context).size.height * 0.5, // 화면 높이의 70% 크기로 설정
                child: Column(
                  children: [
                    AppBar(
                      title: Text('$sendUserEmail님의 메세지', 
                        style: TextStyle(
                          fontFamily: 'NanumSquareRoundEB',
                        )
                      ),
                      backgroundColor: Colors.transparent, // 투명 배경
                    ),
                    AspectRatio(
                      aspectRatio: controller.value.aspectRatio,
                      child: VideoPlayer(controller),
                    ),
                  ],
                ),
              ),
            );
          },
        );

      // 비디오가 초기화되고 나서 자동으로 재생
      controller.play();

      // 비디오 재생이 끝나면 컨트롤러 해제
      controller.addListener(() {
        if (controller.value.position >= controller.value.duration) {
          controller.dispose();
        }
      });
    } catch (e) {
      print('Error playing video: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: Align(
            alignment: Alignment.center,
            child: Text(
              '메세지',
              style: TextStyle(
                fontSize: 24,
                fontFamily: 'NanumSquareRoundEB',
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ),
        Expanded(
          child: messages.isEmpty // 메세지 리스트가 비어있는 경우
          ? Center(
              child: Text('메세지가 없습니다',
                style: TextStyle(
                  fontSize: 18,
                  fontFamily: 'NanumSquareRoundEB',
                  fontWeight: FontWeight.bold,
                )
              ),
            )
          :
            ListView.builder(
              itemCount: messages.length,
              itemBuilder: (context, index) {
                final message = messages[index];

                final videoId = message['videoId'];
                final sendUserEmail = message['sendUserEmail'];

                return Container(
                  width: 390,
                  height: 73,
                  child: ListTile(
                    title: Text('$sendUserEmail',
                      style: TextStyle(fontFamily: 'NanumSquareRoundEB',)),
                    subtitle: Text('영상메세지'),
                    onTap: () {
                      _playVideo(videoId, sendUserEmail);
                    },
                  ),
                );
              },
            ),       
        ),
      ],
    );
  }
}
