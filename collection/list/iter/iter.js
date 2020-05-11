log = console.log;

// iterate list
let numbers = [1, 2, 3];
let objects = { a: 1, b: 2, c: 3 };

for (const e of numbers) {
  log(e);
}

numbers.forEach((e, i) => {
  log(e, i);
});

log('iterate list with index');
for (let i = 0; i < numbers.length; i++) {
  log(numbers[i], i);
}

log('with block');
numbers.forEach((e) => {
  log(e);
});

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
