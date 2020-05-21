main(List<String> args) {
  var l = List(1); // fixed length
  var a = List(); // dynamic length
  var b = List.filled(3, 0);
  var c = List.generate(3, (_) => []);
  a.add(1);
  a.addAll([2, 3]);
  print(a);
  print(b);
  print(c);
}
