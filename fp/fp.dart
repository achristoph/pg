main(List<String> args) {
  var numbers = [1, 2, 3];

  print("filter method");
  print(numbers.where((e) => e > 1));

  print("map method");
  print(numbers.map((e) => e.toString()));

  print("map method - hash type list");
  var h = [
    {"name": 'A'},
    {"name": 'B'},
    {"name": 'C'}
  ];
  print(h.map((e) => e["name"]));

  print("reduce method");
  print(numbers.reduce((a, b) => a + b));
}
