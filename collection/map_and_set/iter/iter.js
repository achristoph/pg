let objects = { a: 1, b: 2, c: 3 };
log = console.log;

log('iterate dictionary with key, value, both');

log('with keys');
for (const k of Object.keys(objects)) {
  log(k);
}

log('with values');
for (const v of Object.values(objects)) {
  log(v);
}

log('with keys and values');
for (const [k, v] of Object.entries(objects)) {
  log(k, v);
}

log('iterate set');
let set = new Set([1, 2, 3]);
for (const e of set) {
  log(e);
}
