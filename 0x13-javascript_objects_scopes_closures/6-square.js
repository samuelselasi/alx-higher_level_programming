#!/usr/bin/node
// A class Square that defines a square and inherits from Rectangle

const Rectangle = require('./5-square');
class Square extends Rectangle {
  charPrint (c) {
    let myChar = '';
    if (c === undefined) {
      myChar = 'X';
    } else {
      myChar = c;
    }
    let i = 0;
    for (i = 0; i < this.height; i++) {
      let row = 0;
      let column = '';
      for (row = 0; row < this.width; row++) {
        column = column + myChar;
      }
      console.log(column);
    }
  }
}
module.exports = Square;
