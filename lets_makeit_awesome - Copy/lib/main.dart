import 'package:flutter/material.dart';
import 'package:lets_makeit_awesome/pages/firstPg.dart';
import 'package:lets_makeit_awesome/pages/secondPg.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  const MyApp({super.key});

  @override
  Widget build(BuildContext context){
    return MaterialApp(
      home: FirstPage(),
      routes: { //creating routes
        './secondpage': (context) => SecondPage(),
      },
    );
  }
}