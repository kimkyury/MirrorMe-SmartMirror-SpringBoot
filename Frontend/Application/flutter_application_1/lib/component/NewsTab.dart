import 'package:flutter/material.dart';

class NewsTab extends StatelessWidget {
  const NewsTab({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2, // 탭의 개수 설정
      child: Scaffold(
        appBar: AppBar(
          title: Text('News Tab'),
          bottom: TabBar(
            tabs: [
              Tab(text: 'Tab 1'),
              Tab(text: 'Tab 2'),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            // 첫 번째 탭의 내용
            Center(
              child: Text('Tab 1 Content'),
            ),
            // 두 번째 탭의 내용
            Center(
              child: Text('Tab 2 Content'),
            ),
          ],
        ),
      ),
    );
  }
}