#!/usr/bin/node
const args = process.argv.slice(2);
const bigest = [0, 0];
args.forEach(element => {
  if (+element > bigest[0]) {
    if (bigest[0]) {
      bigest[1] = bigest[0];
    }
    bigest[0] = +element;
  }
});
console.log(bigest[1]);
