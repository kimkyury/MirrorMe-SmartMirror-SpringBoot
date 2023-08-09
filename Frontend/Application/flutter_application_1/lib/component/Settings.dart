import 'package:flutter/material.dart';

class Settings extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          _buildSettingsItem(context, 'My Profile'),
          _buildSettingsItem(context, 'My Mirror'),
          _buildSettingsItem(context, 'My Favorite'),
          _buildSettingsItem(context, 'FAQ'),
        ],
      ),
    );
  }

  Widget _buildSettingsItem(BuildContext context, String title) {
    return InkWell(
      onTap: () {
        // 각 항목을 눌렀을 때의 동작을 추가하려면 여기에 코드를 작성하세요.
      },
      child: Container(
        padding: EdgeInsets.symmetric(vertical: 20, horizontal: 16),
        decoration: BoxDecoration(
          border: Border(
            bottom: BorderSide(color: Colors.grey.shade300),
          ),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              title,
              style: TextStyle(fontSize: 18),
            ),
            Icon(Icons.arrow_forward_ios),
          ],
        ),
      ),
    );
  }
}
