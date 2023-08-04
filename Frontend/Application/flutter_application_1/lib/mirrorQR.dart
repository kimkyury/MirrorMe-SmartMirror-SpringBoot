import 'package:flutter/material.dart';
import 'dart:io';

class MirrorQR extends StatelessWidget {
  const MirrorQR({super.key});

  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}


class SelectMirrorPlace extends StatefulWidget {
  const SelectMirrorPlace({Key? key}) : super(key: key);

  @override
  _SelectMirrorPlaceState createState() => _SelectMirrorPlaceState();
}

class _SelectMirrorPlaceState extends State<SelectMirrorPlace> {
  String _selectedPlace = ''; // Store the selected place
  TextEditingController _otherPlaceController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          '거울 위치 선택',
          style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
        ),
        SizedBox(height: 10),
        Column(
          children: [
            DropdownButton<String>(
              value: _selectedPlace,
              onChanged: (value) {
                setState(() {
                  _selectedPlace = value!;
                });
              },
              items: ['현관', '거실', '기타']
                  .map<DropdownMenuItem<String>>(
                    (String value) => DropdownMenuItem<String>(
                      value: value,
                      child: Text(value),
                    ),
                  )
                  .toList(),
            ),
            if (_selectedPlace == '기타')
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16.0),
                child: TextField(
                  controller: _otherPlaceController,
                  decoration: InputDecoration(
                    labelText: '기타 위치 입력',
                  ),
                ),
              ),
          ],
        ),
      ],
    );
  }
}