#!/usr/bin/node
// A function that prints no. of args already printed and new argument value

let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
