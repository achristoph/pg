main(List<String> args) {
  var numbers = [1, 2, 3];
  var d = {"a": 1, "b": 2, "c": 3};

  print("iterate list");
  for (var e in numbers) {
    print(e);
  }
  numbers.forEach((e) => print(e));

  print("iterate list with index");
  for (var i = 0; i < numbers.length; i++) {
    print("${numbers[i]} ${i}");
  }

  print('with block');
  numbers.forEach((e) {
    print(e);
  });

  print("iterate dictionary with key, value, both");
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
}
