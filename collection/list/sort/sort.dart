// Comparator functions
byLowerCase(a, b) {
  return a.toLowerCase().compareTo(b.toLowerCase());
}

byLength(a, b) {
  return a.length.compareTo(b.length);
}

main(List<String> args) {
  var a = ['Art', 'b', 'ART'];

  // 1. Creating a new sorted array with a comparator
  var b = a.toList();
  b.sort((a, b) => byLowerCase(a, b));
  print(b);

  // 2. Creating a new sorted array with multiple comparators
  var c = a.toList();
  var sortFunctions = [byLength, byLowerCase];

  c.sort((a, b) {
    var i = 0;
    var r = 0;
    while (r == 0 && i < sortFunctions.length) {
      r = sortFunctions[i++](a, b);
    }
    return r;
  });

  print(c);

  // 3. Sorting array with in-place sort
  a.sort((a, b) => byLowerCase(a, b));
  print(a);

  // 4. Sorting numeric array to string order
  // compareTo function return 0,1,-1 for equal, greater than, less than comparison
  var d = [2, 100, 3];
  d.sort((a, b) => a.toString().compareTo(b.toString()));
  print(d);

  // 5. Sorting string array to numeric order
  var e = ["2", "100", "3"];
  e.sort((a, b) => int.parse(a).compareTo(int.parse(b)));
  print(e);

  // 6. Sorting numeric array
  var f = [3, 1, 2];
  f.sort();
  print(f);
}
