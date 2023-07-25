#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request.get(URL, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const completedTasks = {};

  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 1;
      } else {
        completedTasks[todo.userId] += 1;
      }
    }
  });
  console.log(completedTasks);
});
