#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request.get(URL, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(error);
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

  let task = 0;
  const length = Object.keys(todos).length;
  if (length === 0) {
    console.log('{}');
    return;
  }

  for (const key in todos) {
    if (task === 0) {
      if (length !== 1) {
        console.log('{ \'' + key + '\': ' + todos[key] + ',');
      } else {
        console.log('{ \'' + key + '\': ' + todos[key] + ' }');
      }
    } else if (task === length - 1) {
      console.log('  \'' + key + '\': ' + todos[key] + ' }');
    } else {
      console.log(`  '${key}': ${todos[key]},`);
    }
    task++;
  }
});
