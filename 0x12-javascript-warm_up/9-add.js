#!/usr/bin/node
// A script that prints the addition of 2 integers

const myNum1 = process.argv[2];
const myNum2 = process.argv[3];
const a = parseInt(myNum1, 10);
const b = parseInt(myNum2, 10);

function add (a, b) {
  const sum = a + b;
  return (sum);
}

console.log(add(a, b));
