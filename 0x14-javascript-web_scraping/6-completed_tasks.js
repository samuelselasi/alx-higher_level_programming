#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

request.get(URL, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error occurred while making the request:', error.message);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    return;
  }

  const completedTasks = body.filter((task) => task.completed === true);
  const todos = {};

  completedTasks.forEach((task) => {
    if (!todos[task.userId]) {
      todos[task.userId] = 1;
    } else {
      todos[task.userId]++;
    }
  });

  console.log(todos);
});
