#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (a) {
  if (!a) return 1;
  if (a < 0) return -1;
  if (a === 0 || a === 1) return 1;
  return a * factorial(a - 1);
}

console.log(factorial(+args[0]));
