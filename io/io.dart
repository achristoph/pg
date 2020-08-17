import 'dart:io';

writeFile(File file) {
  RandomAccessFile raf = file.openSync(mode: FileMode.APPEND);
  raf.writeStringSync('Hi');
  raf.flushSync();
  raf.closeSync();
}

readFile(File file) {
  print(file.readAsStringSync());
}

main(List<String> args) {
  Directory currentDir = Directory.current;
  print(currentDir.existsSync());
  print(currentDir.path);
  List list = currentDir.listSync(recursive: true);
  list.forEach((value) {
    FileStat stat = value.statSync();
    // print(stat);
  });

  File file = new File(currentDir.path + '/a.txt');
  print(Platform.operatingSystem);
  print(Platform.version);
  print(Platform.script.path);
  print(Platform.executable);
  // Platform.environment.keys.forEach((key) {
  //   print("$key ${Platform.environment[key]}");
  // });

  Process.run('ls', ['-l']).then((ProcessResult res) {
    print(res.stdout);
    print(res.exitCode);
  });
}
