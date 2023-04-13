#!/usr/bin/node
const args = process.argv.slice(2);

function add(a, b) {
  return a + b;
}

console.log(add(+args[0], +args[1]));
