log = console.log;

// iterate list
let numbers = [1, 2, 3];

for (const e of numbers) {
  log(e);
}

numbers.forEach((e, i) => {
  log(e, i);
});

log('iterate list with index:');
for (let i = 0; i < numbers.length; i++) {
  log(numbers[i], i);
}

log('with block:');
numbers.forEach((e) => {
  log(e);
});

console.log('while loop');
let sum = 0;
while (sum < 3) {
  sum++;
}
console.log(sum);
