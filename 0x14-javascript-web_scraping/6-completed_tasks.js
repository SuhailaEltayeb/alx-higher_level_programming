#!/usr/bin/node

const httpRequest = require('request');
const url = process.argv[2];

httpRequest(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const completedTasks = {};

    JSON.parse(body).forEach(task => {
      if (task.completed) {
        completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
      }
    });

    console.log(completedTasks);
  } else {
    console.log('An error occurred. Status code:', response.statusCode);
  }
});
