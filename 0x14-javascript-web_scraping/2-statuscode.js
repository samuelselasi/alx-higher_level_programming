#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request.get(URL, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
