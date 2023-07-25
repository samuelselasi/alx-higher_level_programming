#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTasks = JSON.parse(body);
    const dict = {};

    for (const index of completedTasks) {
      if (index.completed === true) {
        if (dict[index.userId] === undefined) {
          dict[index.userId] = 0;
        }
        dict[index.userId] += 1;
      }
    }
    console.log(dict);
  }
});
