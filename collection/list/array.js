function byLowerCase(a, b) {
  if (a.toLowerCase() < b.toLowerCase()) return -1;
  if (a.toLowerCase() > b.toLowerCase()) return 1;
  return 0;
}
function byLength(a, b) {
  if (a.length < b.length) return -1;
  if (a.length > b.length) return 1;
  return 0;
}

let a = ['Art', 'b', 'ART'];

// 1. Creating a new sorted array with a comparator
let b = [...a];

b.sort((a, b) => byLowerCase(a, b));
console.log(b);

// 2. Creating a new sorted array with multiple comparators
// Since 0 value is evaluated to false, the OR hack works nicely here
let c = [...a];

c.sort((a, b) => byLength(a, b) || byLowerCase(a, b));
console.log(c);

// 3. Sorting array with in-place sort
a.sort((a, b) => byLowerCase(a, b));
console.log(a);

// 4. Sorting numeric array to string order
let d = [2, 100, 3];
d.sort((a, b) => {
  if (a.toString() < b.toString()) return -1;
  if (a.toString() > b.toString()) return 1;
  return 0;
});
console.log(d);

// 5. Sorting string array to numeric order
var e = ['2', '100', '3'];
e.sort((a, b) => {
  if (Number(a) < Number(b)) return -1;
  if (Number(a) > Number(b)) return 1;
  return 0;
});
console.log(e);
