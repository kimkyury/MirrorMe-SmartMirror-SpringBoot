import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';
import 'dart:convert'; // utf8과 base64Decode를 사용하기 위해 필요합니다.

class WebViewPage extends StatelessWidget {
  final String apiUrl;

  WebViewPage(this.apiUrl);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("구글 로그인"),
      ),
      body: WebView(
        initialUrl: "$apiUrl/auth/google", // Modify the URL as needed
        javascriptMode: JavascriptMode.unrestricted,
        navigationDelegate: (NavigationRequest request) {
          if (request.url.startsWith("$apiUrl/oauth/google/callback")) {
            // Parse the returned data and send it back to the previous screen
            Navigator.pop(context, request.url);
            return NavigationDecision.prevent;
          }
          return NavigationDecision.navigate;
        },
      ),
    );
  }
}
