#!/usr/bin/node
// A script that prints x times “C is fun”

const arg = process.argv[2];
const x = parseInt(arg, 10);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
