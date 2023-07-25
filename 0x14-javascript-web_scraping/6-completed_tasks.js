#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const completedTasks = JSON.parse(body);
    const dict = {};

    for (const task of completedTasks) {
      if (task.completed === true) {
        if (dict[task.userId] === undefined) {
          dict[task.userId] = 0;
        }
        dict[task.userId] += 1;
      }
    }
    console.log(dict);
  }
});
