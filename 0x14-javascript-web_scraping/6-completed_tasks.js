#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTasks = JSON.parse(body);
    const completed = {};

    for (const task of completedTasks) {
      if (task.completed === true) {
        if (task.completed && completed[task.userId] === undefined) {
          completed[task.userId] = 0;
        }
        completed[task.userId] += 1;
      }
    }
    console.log(completed);
  }
});
