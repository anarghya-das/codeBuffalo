import 'package:flutter/material.dart';

class Activities extends StatefulWidget {
  final String _name, _userName;
  Activities(this._name, this._userName);

  @override
  _ActivitiesState createState() => _ActivitiesState(_name, _userName);
}

class _ActivitiesState extends State<Activities> {
  String _name, _userName;

  _ActivitiesState(this._name, this._userName);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        backgroundColor: Color.fromRGBO(93, 142, 155, 1.0),
      ),
      backgroundColor: Color.fromRGBO(93, 142, 155, 1.0),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Align(
              alignment: Alignment.center,
              child: Text(
                "Hello $_name!",
                style: TextStyle(
                    fontFamily: "RobotoMedium",
                    fontSize: 30,
                    color: Colors.white),
              ),
            )
          ],
        ),
      ),
    );
  }
}
