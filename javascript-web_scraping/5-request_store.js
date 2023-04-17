#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const fs = require('fs');

request.get(args[0], (error, response, body) => {
  if (error) console.log(error);
  fs.writeFile(args[1], body.toString(), 'utf8', error => {
    if (error) console.log(error);
  });
});
