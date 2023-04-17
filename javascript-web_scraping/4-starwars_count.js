#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request.get(args[0], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body);
  let countOfAntilles = 0;
  if (films) {
    for (const film of films.results) {
      for (const character of film.characters) {
        if (character.split('/').slice(5, 6)[0] === '18') {
          countOfAntilles += 1;
        }
      }
    }
    console.log(countOfAntilles);
  }
});
