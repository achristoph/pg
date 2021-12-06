// literal constructor
let n = [1, 2, 3];
// creating a copy array with spread syntax
let m = [...n];

let set = new Set([1, 2, 3]);

// Array constructor with a default value
let a1 = Array(2).fill(0);
// caution for default value with object like array since it refers to the same object
a1 = Array(2).fill([]);
// after the push below, the second element is also modified, so use Array.from instead for object type
a1[0].push(1);

// using the following form, the default objects are separate objects
a1 = Array.from(Array(2), () => []);
a1[0].push(1);

// construct a multi-dimensional array
a1 = Array.from(Array(3), () => Array(3));

let a2 = Array(1, 2, 3);
let a3 = Array(...a2);

// Array static methods
let b1 = Array.from(n, (x) => x * 1);
let b2 = Array([1, 2, 3]);
// initialize array from a set
let b3 = Array.from(set);
// initialize array from a map
let map = new Map([
  [1, 1],
  [2, 2],
]);
b3 = Array.from(map);

// initialize with separate values
let b4 = Array.of(1, 2, 3);

// update array element
let c = [1, 2, 4];
c[2] = 3;
// switch array element
[c[0], c[1]] = [c[1], c[0]];

// insert array element
// first
c.unshift(0);
c.unshift(-2, -1);
// last
c.push(4);
c.push(5, 6);
// in between
c.splice(1, 0, '1');
c.splice(2, 0, '2', '3');

// delete array element
// first
c.shift();
// last
c.pop();
// in between, on which index and specify how many
c.splice(2, 1);
