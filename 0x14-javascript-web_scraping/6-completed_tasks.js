#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const data = {};
      for (const todo of todos) {
        if (todo.completed === true) {
          const userId = todo.userId.toString();
          data[userId] = (data[userId] || 0) + 1;
        }
      }
      console.log(data);
    }
  }
});
