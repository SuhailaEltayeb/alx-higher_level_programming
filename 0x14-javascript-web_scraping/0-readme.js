#!/usr/bin/node

const fileSystem = require('fs');
const filePath = process.argv[2];

fileSystem.readFile(filePath, 'utf-8', function (error, content) {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
