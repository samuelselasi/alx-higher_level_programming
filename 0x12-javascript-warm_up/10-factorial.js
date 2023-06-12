#!/usr/bin/node
// A script that computes and prints a factorial

const myNum = process.argv[2];
const num = parseInt(myNum, 10);
function factorial (num) {
  if (isNaN(num) || num === 0) {
    return (1);
  }
  return (num * factorial(num - 1));
}
console.log(factorial(num));
