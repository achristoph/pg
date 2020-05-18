let objects = { a: 1, b: 2, c: 3 };
log = console.log;

let m = new Map([
  ['a', 1],
  ['b', 2],
  ['c', 3],
]);

log('iterate Map. By default, Map is iterable');
for (const e of m) {
  log(e);
}

log('iterate Map with keys');
for (const k of m.keys()) {
  log(k);
}

log('iterate Map with values');
for (const v of m.values()) {
  log(v);
}

log('iterate map with keys and values');
for (const [k, v] of m) {
  log(k, v);
}

log('iterate Map with keys and values');
for (const [k, v] of m.entries()) {
  log(k, v);
}

log('iterate object by default using for-in');
for (const e in objects) {
  log(e);
}

log('iterate object with keys');
for (const k of Object.keys(objects)) {
  log(k);
}

log('iterate object with values');
for (const v of Object.values(objects)) {
  log(v);
}

log('iterate object with keys and values');
for (const [k, v] of Object.entries(objects)) {
  log(k, v);
}

log('iterate set');
let set = new Set([1, 2, 3]);
for (const e of set) {
  log(e);
}
