#!/usr/bin/node

const filename = process.argv[2];
const fileContent = process.argv[3];
const fs = require('fs');

fs.writeFile(filename, fileContent, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
