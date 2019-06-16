import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart';

final String API_URL = "http://10.0.2.2:8000/graphql/";

class Activities extends StatefulWidget {
  final String _name;
  Activities(this._name);

  @override
  _ActivitiesState createState() => _ActivitiesState(_name);
}

class _ActivitiesState extends State<Activities> {
  String _name;

  _ActivitiesState(this._name);

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
            Text(
              "Recomended Activities for @$_name!",
              textAlign: TextAlign.center,
              style: TextStyle(
                  fontFamily: "RobotoMedium",
                  fontSize: 27,
                  color: Colors.white),
            ),
            FutureBuilder(
              future: getTaskList(),
              builder: (context, snapshot) {
                switch (snapshot.connectionState) {
                  case ConnectionState.none:
                  case ConnectionState.active:
                  case ConnectionState.waiting:
                    return Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: Center(
                            child: CircularProgressIndicator(
                              backgroundColor: Theme.of(context).accentColor,
                            ),
                          ),
                        ),
                        Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: Text("Please wait, Loading Activities..."),
                        )
                      ],
                    );
                  case ConnectionState.done:
                    if (snapshot.hasError) {
                      print(snapshot.error);
                      return Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: <Widget>[
                          Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: Center(
                              child: Text(
                                "An error Occured!",
                                style: TextStyle(fontSize: 30),
                              ),
                            ),
                          )
                        ],
                      );
                    } else {
                      return createActivityList(context, snapshot);
                    }
                }
              },
            )
          ],
        ),
      ),
    );
  }

  Future<List<String>> getTaskList() async {
    Map<String, String> data = new Map<String, String>();
    data["query"] = '{mutation{ sendText(text: \"$_name\"){ text } }"}';
    final response = await post(API_URL, body: data);
    final jsonResponse = json.decode(response.body);
    String ac = jsonResponse['data']['showActivities']['activities'];
    List<String> activities = ac.split("|");
    return activities;
  }

  Widget createActivityList(context, snapshot) {
    List<String> activities = snapshot.data;
    return ListView.separated(
        itemCount: activities.length,
        separatorBuilder: (context, i) => Divider(
              height: 1,
              color: Colors.black26,
            ),
        itemBuilder: (context, i) {
          return ListTile(
            title: Text(activities[i]),
          );
        });
  }
}
