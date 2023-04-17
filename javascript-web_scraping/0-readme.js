#!/usr/bin/node
const fs = require('fs');
fs.readFile('testfile', 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data.toString());
  }
});
