import "package:flutter/material.dart";

class Connect extends StatelessWidget {
  const Connect({super.key});

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
      body: Center(
        child: Text('This is the Connect Page'),
      ),
    );
  }
}