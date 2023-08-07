import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';
import 'dart:convert'; // utf8과 base64Decode를 사용하기 위해 필요합니다.

class WebViewPage extends StatelessWidget {
  String apiUrl ="192.168.30.142:8080";

  WebViewPage(this.apiUrl);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('로그인')),
      body: WebView(
        initialUrl: '$apiUrl/login/oauth',
        javascriptMode: JavascriptMode.unrestricted,
        navigationDelegate: (NavigationRequest request) {
          if (request.url.startsWith('iot://callback')) {
            var token = Uri.parse(request.url).queryParameters['token']!;
            var decodedData = utf8.decode(base64Decode(token));
            print(decodedData);
            
            // 웹뷰 페이지를 닫고 다른 작업을 수행하려면 여기에 로직 추가
            Navigator.pop(context, decodedData); // decodedData를 반환하면서 페이지 닫기
            return NavigationDecision.prevent;
          }
          return NavigationDecision.navigate;
        },
      ),
    );
  }
}
