#!/usr/bin/node
let numberOfPrints = process.argv[2];
if (numberOfPrints) {
  while (numberOfPrints) {
    console.log('C is fun');
    numberOfPrints -= 1;
  }
} else {
  console.log('Missing number of occurrences');
}
