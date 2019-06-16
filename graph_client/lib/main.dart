import 'package:flare_flutter/flare_actor.dart';
import 'package:flutter/material.dart';
import 'package:graph_client/Activities.dart';
import 'teddy_controller.dart';
import 'package:flutter/rendering.dart';
import 'tracking_text_input.dart';
import 'signin_button.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'The Unbored!',
        theme: ThemeData(
            // This is the theme of your application.
            //
            // Try running your application with "flutter run". You'll see the
            // application has a blue toolbar. Then, without quitting the app, try
            // changing the primarySwatch below to Colors.green and then invoke
            // "hot reload" (press "r" in the console where you ran "flutter run",
            // or simply save your changes to "hot reload" in a Flutter IDE).
            // Notice that the counter didn't reset back to zero; the application
            // is not restarted.
            primarySwatch: Colors.green),
        home: Home());
  }
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  TeddyController _teddyController;
  String _name = "";

  @override
  initState() {
    _teddyController = TeddyController();
    super.initState();
  }

  Widget build(BuildContext context) {
    EdgeInsets devicePadding = MediaQuery.of(context).padding;
    return Scaffold(
      appBar: AppBar(
        title: Text("The Unbored!"),
        elevation: 0,
        centerTitle: true,
        backgroundColor: Color.fromRGBO(93, 142, 155, 1.0),
      ),
      backgroundColor: Color.fromRGBO(93, 142, 155, 1.0),
      body: Container(
          child: Stack(
        children: <Widget>[
          Positioned.fill(
              child: Container(
            decoration: BoxDecoration(
              // Box decoration takes a gradient
              gradient: LinearGradient(
                // Where the linear gradient begins and ends
                begin: Alignment.topRight,
                end: Alignment.bottomLeft,
                // Add one stop for each color. Stops should increase from 0 to 1
                stops: [0.0, 1.0],
                colors: [
                  Color.fromRGBO(170, 207, 211, 1.0),
                  Color.fromRGBO(93, 142, 155, 1.0),
                ],
              ),
            ),
          )),
          Positioned.fill(
            child: SingleChildScrollView(
                padding: EdgeInsets.only(
                    left: 20.0, right: 20.0, top: devicePadding.top + 50),
                child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: <Widget>[
                      Container(
                          height: 200,
                          padding:
                              const EdgeInsets.only(left: 30.0, right: 30.0),
                          child: FlareActor(
                            "assets/Teddy.flr",
                            shouldClip: false,
                            alignment: Alignment.bottomCenter,
                            fit: BoxFit.contain,
                            controller: _teddyController,
                          )),
                      Container(
                          decoration: BoxDecoration(
                              color: Colors.white,
                              borderRadius:
                                  BorderRadius.all(Radius.circular(25.0))),
                          child: Padding(
                            padding: const EdgeInsets.all(30.0),
                            child: Form(
                                child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              crossAxisAlignment: CrossAxisAlignment.center,
                              children: <Widget>[
                                TrackingTextInput(
                                    label: "Twitter Username",
                                    hint: "What's your username?",
                                    onTextChanged: (String value) {
                                      _name = value;
                                      debugPrint(_name);
                                    },
                                    onCaretMoved: (Offset caret) {
                                      _teddyController.lookAt(caret);
                                    }),
                                SigninButton(
                                    child: Text("Start",
                                        style: TextStyle(
                                            fontFamily: "RobotoMedium",
                                            fontSize: 18,
                                            color: Colors.white)),
                                    onPressed: () {
                                      if (_name.isEmpty) {
                                        _showSnack();
                                      } else {
                                        Navigator.push(
                                            context,
                                            MaterialPageRoute(
                                                builder: (context) =>
                                                    Activities(
                                                      _name,
                                                    )));
                                      }
                                      // _teddyController.submitPassword();
                                    })
                              ],
                            )),
                          )),
                    ])),
          ),
        ],
      )),
    );
  }

  void _showSnack() {
    Scaffold.of(context).showSnackBar(SnackBar(
      content: Text("Please enter your details properly! :("),
    ));
  }
}
