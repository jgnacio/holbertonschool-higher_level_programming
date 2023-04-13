#!/usr/bin/node
const argsNumber = process.argv.slice(2).length;
if (argsNumber === 0) {
  console.log('No argument');
} else if (argsNumber === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
