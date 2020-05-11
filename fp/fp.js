log = console.log;

let numbers = [1, 2, 3];

log('filter method');
log(numbers.filter((e) => e > 1));

log('map method');
log(numbers.map((e) => e.toString()));

log('map method - hash type list');
d = [{ name: 'A' }, { name: 'B' }, { name: 'C' }];
log(d.map((e) => e.name));

log('reduce method');
log(numbers.reduce((a, b) => a + b));
