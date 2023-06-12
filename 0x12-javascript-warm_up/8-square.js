#!/usr/bin/node
// A script that prints a square

const arg = process.argv[2];
const size = parseInt(arg, 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;
  for (i = 0; i < size; i++) {
    let row = 0;
    let column = '';
    for (row = 0; row < size; row++) {
      column = column + 'X';
    }
    console.log(column);
  }
}
