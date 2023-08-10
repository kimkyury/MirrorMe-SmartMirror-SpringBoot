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
      ),
      body: Center(
        child: Text('This is the Connect Page'),
      ),
    );
  }
}