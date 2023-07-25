#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');
const dict = {};

request.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body);
    for (const task of result) {
      if (task.completed === true) {
        const ID = task.userId;
        if (!dict[ID]) {
          dict[ID] = 1;
        } else {
          dict[ID] += 1;
        }
      }
    }
    console.log(dict);
  }
});
