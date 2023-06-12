#!/usr/bin/node
/* A script that prints 3 lines: by using an array of string and a loop
 * The first line: “C is fun”
 * The second line: “Python is cool”
 * The third line: “JavaScript is amazing”
 */

const myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
for (i = 0; i < 3; i++) {
  console.log(myArray[i]);
}
