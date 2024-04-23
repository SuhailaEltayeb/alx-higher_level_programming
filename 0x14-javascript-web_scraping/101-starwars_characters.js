#!/usr/bin/node

const httpRequest = require('request');
const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

httpRequest.get(apiUrl + filmId, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters);
  }
});

function printCharacters(characters) {
  characters.forEach(characterUrl => {
    httpRequest.get(characterUrl, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        console.log(JSON.parse(body).name);
      }
    });
  });
}
