import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:path_provider/path_provider.dart'; // path_provider 패키지 임포트
import 'package:video_player/video_player.dart';
import 'dart:io';
import 'dart:convert';

class Message extends StatelessWidget {

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
      body: MessageListView(),
    );
  }
}

class MessageListView extends StatefulWidget {

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
    
    // String accessToken = 'ya29.a0AfB_byDgekAtBNbBvXv2U_k2beWGeFig1riSIwnUMjGsMrNPeLvobC8SzflAAahddaOwSaAQCrCYTO61T873QelF9wnfmZsYfJam5w0zb892BFKcJiG0KdEvaWhS0pe2GHIFPWu44VlkCfIFZYtIl2jXrDxdVK3saCgYKAYoSARISFQHsvYlscmPmaHddHNDhwF2EReRftA0167';
    // String refreshToken = '1//0evNs0GmidlHhCgYIARAAGA4SNwF-L9Ir3sLRMdYucUhG6XF4P0UTM2Erq6hW3sbB7JO88F60_qPdxuf_7dtKNflysCcqWLCrtQo';

    var headers = {
      'access_token': 'ya29.a0AfB_byAtQFrmC7N1ho6S8qUcj5UXjin1MNzOXdZThDIMKS7Tq5TzueRt_H9lpfHcT36QhSrXRypnZmZL_knk2R7BwStocQdKVmM4yxnfkCx_vHZFVXwkiHEWZZ8-vyoJl82Yjup583THaCyCC39LTYMSj0L5CFu4Pi-BcNpuTwaCgYKARoSARISFQHsvYlssKoPXSgSAR9qqJJTB8yESQ0177', // access_token 추가
    };

    var cookies = {
      'refresh_token': '1//0evNs0GmidlHhCgYIARAAGA4SNwF-L9Ir3sLRMdYucUhG6XF4P0UTM2Erq6hW3sbB7JO88F60_qPdxuf_7dtKNflysCcqWLCrtQo', // refresh_token을 쿠키에 추가
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
                      title: Text('$sendUserEmail님의 메세지'),
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
          child: ListView.builder(
            itemCount: messages.length,
            itemBuilder: (context, index) {
              final message = messages[index];

              final videoId = message['videoId'];
              final sendUserEmail = message['sendUserEmail'];

              return messages.isEmpty
                  ? Center(
                      child: Text('메세지가 없습니다'),
                    )
                  : Container(
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

// class Message extends StatefulWidget {
//   @override
//   _MessageState createState() => _MessageState();
// }

// class _MessageState extends State<Message> {
//   VideoPlayerController? _controller; // Nullable로 변경

//   @override
//   void initState() {
//     super.initState();
//     // 비디오 URL 설정
//     String videoUrl = "http://i9e101.p.ssafy.io:8080/api/iot/message?videoId=10"; // 실제 URL로 변경해야 함

//     // 비디오 데이터 다운로드 후 비디오 재생
//     _initializeVideoPlayer(videoUrl);
//   }

//   Future<void> _initializeVideoPlayer(String videoUrl) async {
//     // 비디오 데이터 다운로드
//     final response = await http.get(Uri.parse(videoUrl));
//     final videoData = response.bodyBytes;

//     // 임시 디렉토리 얻기
//     final tempDir = await getTemporaryDirectory();

//     // 임시 파일 생성
//     final videoFile = File('${tempDir.path}/tempVideo.mp4');
//     await videoFile.writeAsBytes(videoData);

//     // VideoPlayerController 초기화 및 재생
//     _controller = VideoPlayerController.file(videoFile)
//       ..initialize().then((_) {
//         setState(() {});
//         _controller!.play(); // null 체크 후 접근
//       });
//   }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Image.asset('lib/assets/MirrorMe_Main.png'),
//         backgroundColor: Colors.white,
//         centerTitle: true,
//         leading: IconButton(
//           icon: Image.asset('lib/assets/back.png'), // 원하는 이미지로 대체
//           onPressed: () {
//             Navigator.of(context).pop(); // 뒤로 가기 기능 실행
//           },
//         ),
//       ),
//       body: Center(
//         child: _controller?.value.isInitialized ?? false
//             ? AspectRatio(
//                 aspectRatio: _controller!.value.aspectRatio,
//                 child: VideoPlayer(_controller!),
//               )
//             : CircularProgressIndicator(), // 비디오가 준비되기 전에 로딩 표시
//       ),
//       floatingActionButton: FloatingActionButton(
//         onPressed: () {
//           if (_controller != null) {
//             if (_controller!.value.isPlaying) {
//               _controller!.pause();
//             } else {
//               _controller!.play();
//             }
//           }
//         },
//         child: Icon(
//           _controller?.value.isPlaying ?? false
//               ? Icons.pause
//               : Icons.play_arrow,
//         ),
//       ),
//     );
//   }

//   @override
//   void dispose() {
//     super.dispose();
//     _controller?.dispose(); // null 체크 후 해제
//   }
// }
