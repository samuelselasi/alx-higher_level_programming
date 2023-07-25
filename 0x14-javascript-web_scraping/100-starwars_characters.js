#!/usr/bin/node

const ID = process.argv[2];
const URL = `https://swapi.dev/api/films/${ID}/`;
const request = require('request');

request.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const content = JSON.parse(body);
  const chars = content.characters;

  for (const character of chars) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }

      const charContent = JSON.parse(body);
      console.log(charContent.name);
    });
  }
});
