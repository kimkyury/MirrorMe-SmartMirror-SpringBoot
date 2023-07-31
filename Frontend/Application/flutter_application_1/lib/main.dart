import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('M', style: TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.w600
          ),),
        actions: [
          Icon(Icons.message), // 메세지
          Icon(Icons.connect_without_contact) // 연결
        ],),
        body: Container(
          // 라우터 뷰 추가
        ),
        bottomNavigationBar: BottomAppBar(
          child: Container(
            padding: EdgeInsets.all(20),
            height: 80,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Column(
                  children: [
                    Icon(Icons.newspaper, color: Colors.blue,),
                    Text('뉴스', style: TextStyle(fontSize: 10, color: Colors.blue),)
                  ],),
                Column(
                  children: [
                    Icon(Icons.emoji_emotions, color: Colors.blue,),
                    Text('감정', style: TextStyle(fontSize: 10, color: Colors.blue),)
                  ],),
                Column(
                  children: [
                    Icon(Icons.home, color: Colors.blue,),
                    Text('홈', style: TextStyle(fontSize: 10, color: Colors.blue),)
                  ],),
                Column(
                  children: [
                    Icon(Icons.people, color: Colors.blue,),
                    Text('가족', style: TextStyle(fontSize: 10, color: Colors.blue),)
                  ],),
                Column(
                  children: [
                    Icon(Icons.settings, color: Colors.blue,),
                    Text('설정', style: TextStyle(fontSize: 10, color: Colors.blue),)
                  ],),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
