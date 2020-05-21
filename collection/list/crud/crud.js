let n = [1, 2, 3];
let m = [...n];
let set = new Set([1, 2, 3]);

// Array constructor with a default value
let a1 = Array(1).fill(0);
a1.push(1, 2, 2, 3, 5);

let a2 = Array(1, 2, 3);
let a3 = Array(...a2);

// Array static methods
let b1 = Array.from(n, (x) => x * 1);
let b2 = Array([1, 2, 3]);
let b3 = Array.from(set);
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
// in between
c.splice(1, 1);
