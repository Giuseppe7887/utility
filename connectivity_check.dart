import 'dart:async';
import 'package:http/http.dart' as http;
import 'package:connectivity_plus/connectivity_plus.dart';

Stream<bool> ConnectionStream() {
  StreamController<bool> controller = StreamController<bool>();

  bool state = true;
  Timer.periodic(Duration(seconds: 2), (Timer timer) {
    // se non raggiungi google non hai internet
    http.get(Uri.parse("https://google.com")).then((res) {
      bool localState = res.statusCode == 200;
      if (localState != state) {
        state = localState;
        controller.add(localState);
      }
    }).catchError((err) {
      bool localState = false;
      if (localState != state) {
        state = localState;
        controller.add(localState);
      }
    });
  });
  Connectivity()
      .onConnectivityChanged
      .listen((List<ConnectivityResult> result) {
    bool localState = result.contains(ConnectivityResult.wifi) ||
        result.contains(ConnectivityResult.mobile);
    if (localState != state) {
      state = localState;
      controller.add(localState);
    }
  });

  return controller.stream;
}
