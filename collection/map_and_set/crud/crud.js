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
map.clear();
