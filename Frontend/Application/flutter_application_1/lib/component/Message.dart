import 'package:flutter/material.dart';

class Message extends StatelessWidget {
  const Message({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Message Page'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          SizedBox(height: 20),
          Text(
            'This is the Message Page',
            style: TextStyle(fontSize: 18),
          ),
          SizedBox(height: 20),
          Expanded(
            child: ListView.builder(
              itemCount: 10, // 메시지 목록의 아이템 개수
              itemBuilder: (BuildContext context, int index) {
                return ListTile(
                  title: Text('메시지 $index'),
                  subtitle: Text('메시지 내용 $index'),
                  onTap: () {
                    // 메시지 목록의 아이템을 눌렀을 때의 동작을 추가하려면 여기에 코드를 작성하세요.
                  },
                );
              },
            ),
          ),
          ElevatedButton(
            onPressed: () {
              // 메시지 보내기 버튼을 눌렀을 때의 동작을 추가하려면 여기에 코드를 작성하세요.
            },
            child: Text('메시지 보내기'),
          ),
        ],
      ),
    );
  }
}
