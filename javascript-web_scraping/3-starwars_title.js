#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request.get(
  `https://swapi-api.alx-tools.com/api/films/${args[0]}/`,
  (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const json = JSON.parse(body);
    if (json) console.log(json.title);
  }
);
