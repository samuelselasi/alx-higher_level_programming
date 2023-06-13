#!/usr/bin/node
// A class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      let row = 0;
      let column = '';
      for (row = 0; row < this.width; row++) {
        column = column + 'X';
      }
      console.log(column);
    }
  }
}
module.exports = Rectangle;
