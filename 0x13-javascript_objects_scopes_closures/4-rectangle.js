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

  rotate () {
    let tmp = 0;
    tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
