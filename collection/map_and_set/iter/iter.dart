main(List<String> args) {
  var d = {"a": 1, "b": 2, "c": 3};

  print("with keys");
  for (var k in d.keys) {
    print(k);
  }
  print("with values");
  for (var v in d.values) {
    print(v);
  }
  print("with keys and values");
  for (var e in d.entries) {
    print("${e.key} ${e.value}");
  }

  print("iterate set");
  Set set = new Set.from([1, 2, 3]);
  for (var e in set) {
    print(e);
  }
}
