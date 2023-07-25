#!/usr/bin/node

const URL = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
