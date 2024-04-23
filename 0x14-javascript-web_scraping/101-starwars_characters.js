#!/usr/bin/node

const httpRequest = require('request');
const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

httpRequest.get(apiUrl + filmId, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    printCharacterNames(characters);
  }
});

function printCharacterNames(characters) {
  let count = 0;

  function next() {
    if (count < characters.length) {
      const characterUrl = characters[count];
      httpRequest.get(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
          count++;
          next();
        }
      });
    }
  }

  next();
}
