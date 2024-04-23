#!/usr/bin/node

const fileSystem = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fileSystem.writeFile(filePath, stringToWrite, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
