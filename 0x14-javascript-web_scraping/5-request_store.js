#!/usr/bin/node

const httpRequest = require('request');
const fileSystem = require('fs');

const sourceUrl = process.argv[2];
const destinationFile = process.argv[3];

httpRequest.get(sourceUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fileSystem.writeFileSync(destinationFile, body);
  }
});
