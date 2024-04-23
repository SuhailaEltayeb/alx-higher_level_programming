#!/usr/bin/node

const httpRequest = require('request');
const targetURL = process.argv[2];

httpRequest.get(targetURL, function (error, httpResponse) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', httpResponse.statusCode);
  }
});
