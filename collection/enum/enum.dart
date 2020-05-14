enum Color { red, green, blue }

main(List<String> args) {
  // Color.red is an enum type
  print(Color.red);
  // Value can be converted to string
  print(Color.red.toString());
  // enum type has index property starting at 0
  print(Color.red.index);

  // enum type is hashable
  var m = Map();
  m[Color.red] = 1;
  print(m[Color.red]);
}
