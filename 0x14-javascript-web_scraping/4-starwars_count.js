#!/usr/bin/node

const httpRequest = require('request');
const targetUrl = process.argv[2];

httpRequest(targetUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes('18')) {
          count++;
        }
      });
    });

    console.log(count);
  } else {
    console.log('An error occurred. Status code:', response.statusCode);
  }
});
