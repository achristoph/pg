l = console.log;

let map = new Map([
  ['a', 1],
  ['b', 1],
]);

map.set('c', 1);
map.get('a');
map.delete('c');
map.has('c');
map.size;

// iterate by key, value and both
for (const [k, v] of map.entries()) {
  l(k, v);
}
for (const [k, v] of map.keys()) {
  l(k, v);
}
for (const [k, v] of map.values()) {
  l(k, v);
}

map.clear();
