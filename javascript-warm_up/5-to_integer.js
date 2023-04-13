#!/usr/bin/node
const args = process.argv.slice(2);
+args[0] ?? undefined == undefined
  ? console.log(`My number: ${+args[0]}`)
  : console.log("Not a number");
