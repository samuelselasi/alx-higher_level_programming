#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request.get(URL, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    return;
  }

  const todos = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!todos[todo.userId]) {
        todos[todo.userId] = 1;
      } else {
        todos[todo.userId]++;
      }
    }
  });

  const length = Object.keys(todos).length;
  if (length === 0) {
    console.log('{}');
    return;
  }

  let task = 0;
  console.log('{');
  Object.entries(todos).forEach(([key, value]) => {
    if (task === length - 1) {
      console.log(`  '${key}': ${value}`);
    } else {
      console.log(`  '${key}': ${value},`);
    }
    task++;
  });
  console.log('}');
});
