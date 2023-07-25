#!/usr/bin/node

const filename = process.argv[2];
const fs = require('fs');

fs.readFile(filename, 'utf-8', (error, fileContent) => {
  if (error) {
    console.log(error);
  } else {
    console.log(fileContent);
  }
});
