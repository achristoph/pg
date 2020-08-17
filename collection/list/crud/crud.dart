main(List<String> args) {
  var l = List(1); // fixed length
  var a = List(); // dynamic length
  a = List.filled(3, 0);
  a = List.generate(3, (_) => []);

// insert element
  a.add(1);
  a.addAll([2, 3]);

// update element

// delete element
}
