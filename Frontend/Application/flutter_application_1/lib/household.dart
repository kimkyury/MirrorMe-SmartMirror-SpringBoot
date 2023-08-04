import 'package:flutter/material.dart';
import './mirrorQR.dart';


class HouseHold extends StatefulWidget {
  const HouseHold({Key? key}) : super(key: key);

  @override
  _HouseHoldState createState() => _HouseHoldState();
}

class _HouseHoldState extends State<HouseHold> {
  final TextEditingController _householdNameController = TextEditingController();
  final TextEditingController _searchUserEmailController = TextEditingController();

  bool _isSearching = false;
  String _searchResult = '';

  void _createHousehold() {
    String householdName = _householdNameController.text;
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => MirrorQR(),
      ),
    );
    // TODO: Implement POST API 4-1 to create a household with householdName
  }

  void _searchHousehold() {
    String userEmail = _searchUserEmailController.text;
    // TODO: Implement POST API 4-2 to search for a household by createUser's userEmail
    // TODO: Set _searchResult based on the API response
  }

  @override
  void dispose() {
    _householdNameController.dispose();
    _searchUserEmailController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('HouseHold'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            _isSearching
                ? Text('Search Result: $_searchResult')
                : Column(
                    children: [
                      TextField(
                        controller: _householdNameController,
                        decoration: InputDecoration(
                          labelText: '가정 이름 입력',
                        ),
                      ),
                      ElevatedButton(
                        onPressed: _createHousehold,
                        child: Text('가정 생성'),
                      ),
                    ],
                  ),
            SizedBox(height: 20),
            TextField(
              controller: _searchUserEmailController,
              decoration: InputDecoration(
                labelText: '찾을 가정의 생성자 이메일 입력',
              ),
            ),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  _isSearching = true;
                  _searchHousehold();
                });
              },
              child: Text('가정 검색'),
            ),
          ],
        ),
      ),
    );
  }
}