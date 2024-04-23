#!/usr/bin/node

const request = require('request');
const episodeNumber = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(apiUrl + episodeNumber, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const responseData = JSON.parse(body);
    console.log(responseData.title);
  } else {
    console.log('Error code:', response.statusCode);
  }
});
