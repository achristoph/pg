// Javascript does not have enum, but Typescript does
// There are numeric, string enum

console.log('numeric enum');
enum Color {
  Red,
  Green,
  Blue,
}

console.log('string enum');
enum Answer {
  No = '1',
  Yes = '2',
}

console.log('enum name and value are printable');
console.log(Color.Red.valueOf());
console.log(Color.Red);
console.log(Color[Color.Red]);

console.log('enum is hashable');
let m = new Map();
m.set(Color.Red, 1);
console.log(m.get(Color.Red));
