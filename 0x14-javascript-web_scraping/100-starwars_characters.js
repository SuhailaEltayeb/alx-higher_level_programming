#!/usr/bin/node

const httpRequest = require('request');
const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

httpRequest.get(apiUrl + filmId, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach(characterUrl => {
      httpRequest.get(characterUrl, function (error, response, characterBody) {
        if (error) {
          console.error(error);
        } else {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
