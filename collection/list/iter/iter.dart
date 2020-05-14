main(List<String> args) {
  var numbers = [1, 2, 3];

  print("iterate list:");
  for (var e in numbers) {
    print(e);
  }
  numbers.forEach((e) => print(e));

  print("iterate list with index:");
  for (var i = 0; i < numbers.length; i++) {
    print("${numbers[i]} ${i}");
  }

  print('iterate with block for multiline');
  numbers.forEach((e) {
    // do more things
    print(e);
  });

  print('while loop');
  var sum = 0;
  while (sum < 3) {
    sum++;
  }
  print(sum);
}
