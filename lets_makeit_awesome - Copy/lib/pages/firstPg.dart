import 'package:flutter/material.dart';
import 'package:lets_makeit_awesome/pages/secondPg.dart';

class FirstPage extends StatelessWidget { //press ctrl+ . to make it stateful
  const FirstPage({super.key});

// Just like react useState we have states here too as setState,getState.
  @override
  Widget build(BuildContext context){
    return Scaffold(
      // appBar: AppBar(title: Text("1st page")),
      body: Center(
        child: ElevatedButton(child: Text("PG-2"),
        onPressed: (){
          // Navigator.push(context,
          // MaterialPageRoute(builder: (context) => SecondPage(),),);
          Navigator.pushNamed(context, './secondpage'); //naming routes
        },
        ),
      ),

      // drawer: Drawer( //Dominoes style popup
      //   backgroundColor: Colors.lightBlue[200],
      //   child: Column(children: [
      //     DrawerHeader(child: Icon(
      //       Icons.person,
      //       size: 40,
      //     )),
      //     ListTile(
      //       leading: Icon(Icons.home),
      //       title: Text("Home"),
      //       onTap: (){
      //         Navigator.pop(context); //Pops the drawer
      //       },
      //     ),
      //     ListTile(
      //       leading: Icon(Icons.home),
      //       title: Text("Home"),
      //       onTap: (){
      //       },
      //     ),
      //     ListTile(
      //       leading: Icon(Icons.home),
      //       title: Text("Home"),
      //       onTap: (){
      //       },
      //     )
      //   ],)
      // ),

      bottomNavigationBar: BottomNavigationBar(items: [
        BottomNavigationBarItem(
          icon: Icon(Icons.home),
          label: 'Home',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.person),
          label: 'Home',
        ),
      ]),

    );
  }
}