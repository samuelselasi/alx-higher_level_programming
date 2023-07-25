#!/usr/bin/node

const ID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;
const request = require('request');

request.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
