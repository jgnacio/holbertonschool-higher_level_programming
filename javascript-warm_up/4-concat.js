#!/usr/bin/node
const args = process.argv.slice(2);
console.log(
  [args[0] ? args[0] : 'undefined', args[1] ? args[1] : 'undefined'].join(
    ' is '
  )
);
