import 'package:flutter/material.dart';
import 'package:lets_makeit_awesome/pages/firstPg.dart';

class SecondPage extends StatefulWidget {
  const SecondPage({super.key});

  @override
  State<SecondPage> createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {

  TextEditingController myText = TextEditingController(); //stores text
  
  String greetingMsg = "";
  void greetUser(){
    String username = myText.text;
    setState(() {
      greetingMsg = "Hey " + username;
    }); //rebuilds widget if new name comes
    // print(myText.text);
  }

  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(title: Text("2nd page")),

      // User inputting
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(25),

        child: Column(children: [
        Text(greetingMsg), //directly printing input to the app
        TextField(
          controller: myText,
          decoration: InputDecoration(
            border: OutlineInputBorder(),
            hintText: "Type your name here",
          ),
        ),
        ElevatedButton(onPressed: greetUser, child: Text("Tap")
        ),

        ],)
        )
      )
    );
  }
}