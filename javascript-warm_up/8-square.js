#!/usr/bin/node
const args = process.argv.slice(2);

const squareSize = +args[0];

if (squareSize) {
  for (let i = 0; i < squareSize; i++) {
    for (let j = 0; j < squareSize; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
