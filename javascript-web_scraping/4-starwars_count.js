#!/usr/bin/node
const request = require('request');

request.get(
  'https://swapi-api.alx-tools.com/api/films/',
  (error, response, body) => {
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
  }
);
