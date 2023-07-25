#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    return;
  }

  const data = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!data[todo.userId]) {
        data[todo.userId] = 1;
      } else {
        data[todo.userId]++;
      }
    }
  });
  let index = 0;
  const length = Object.keys(data).length;
  if (length === 0) {
    console.log('{}');
    return;
  }
  for (const key in data) {
    if (index === 0) {
      if (length !== 1) {
        console.log('{ \'' + key + '\': ' + data[key] + ',');
      } else {
        console.log('{ \'' + key + '\': ' + data[key] + ' }');
      }
    } else if (index === length - 1) {
      console.log('  \'' + key + '\': ' + data[key] + ' }');
    } else {
      console.log(`  '${key}': ${data[key]},`);
    }
    index++;
  }
});
