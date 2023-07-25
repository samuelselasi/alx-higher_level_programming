#!/usr/bin/node

const ID = process.argv[2];
const URL = `https://swapi.dev/api/films/${ID}/`;
const request = require('request');

let chars = [];

request.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const content = JSON.parse(body);
  chars = content.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === chars.length) {
    return;
  }

  request(chars[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }

    const charContent = JSON.parse(body);
    console.log(charContent.name);
    getCharacters(index + 1);
  });
};
