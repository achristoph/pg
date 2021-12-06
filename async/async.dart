import 'dart:async';
import 'dart:io';

int count = 0;
String getTime() {
  DateTime dt = DateTime.now();
  return dt.toString();
}

void timeout(Timer timer) {
  print(getTime());
  count++;
  if (count >= 3) timer.cancel();
}

Future<File> appendFile() {
  File file = new File(Directory.current.path + '/a.txt');
  return file.writeAsString('x');
}

main(List<String> args) async {
  Duration duration = Duration(seconds: 1);
  Timer timer = Timer.periodic(duration, timeout);
  File file = await appendFile();
  print(file);
}
