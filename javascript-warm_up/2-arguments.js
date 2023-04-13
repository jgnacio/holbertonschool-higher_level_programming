#!/usr/bin/node
process.argv.slice(2).length > 0
  ? console.log('Argument found')
  : console.log('No argument');
