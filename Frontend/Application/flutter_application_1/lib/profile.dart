import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';

import './household.dart';


class Profile extends StatefulWidget {
  const Profile({Key? key}) : super(key: key);

  @override
  _ProfileState createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {
  TextEditingController _nameController = TextEditingController();
  String _name = '';

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }

  void _navigateToNextPage() {
    if (_name.isNotEmpty) {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => ProfilePicture()),
      );
    } else {
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text('이름 입력 오류'),
            content: Text('이름을 입력해주세요.'),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: Text('확인'),
              ),
            ],
          );
        },
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Profile'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              '본인 이름: $_name',
              style: TextStyle(fontSize: 20),
            ),
            SizedBox(height: 20),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: TextField(
                controller: _nameController,
                onChanged: (value) {
                  setState(() {
                    _name = value;
                  });
                },
                decoration: InputDecoration(
                  labelText: '이름 입력',
                  border: OutlineInputBorder(),
                ),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _navigateToNextPage,
              child: Text('Next'),
            ),
          ],
        ),
      ),
    );
  }
}

class ProfilePicture extends StatefulWidget {
  const ProfilePicture({Key? key}) : super(key: key);

  @override
  _ProfilePictureState createState() => _ProfilePictureState();
}

class _ProfilePictureState extends State<ProfilePicture> {
  late ImagePicker _imagePicker;
  XFile? _imageFile;

  @override
  void initState() {
    super.initState();
    _imagePicker = ImagePicker();
  }

  void _pickImageFromCamera() async {
    XFile? pickedFile = await _imagePicker.pickImage(
      source: ImageSource.camera,
    );

    if (pickedFile != null) {
      setState(() {
        _imageFile = pickedFile;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Profile Picture'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            _imageFile != null
                ? Image.file(
                    File(_imageFile!.path),
                    height: 200,
                    width: 200,
                  )
                : Text(
                    '프로필 사진을 촬영해주세요!',
                    style: TextStyle(fontSize: 20),
                  ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _pickImageFromCamera,
              child: Text('촬영하기'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => HouseHold()),
                );
              },
              child: Text('다음 단계'),
            ),
          ],
        ),
      ),
    );
  }
}
