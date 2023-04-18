#!/usr/bin/node

// Exercise 3: make an Rectangle class
// with 'width' and 'height' fields,
// and a constructor that takes args 'w' and 'h'
// and assigns 'w' to 'width'
// and 'h' to 'height'.

// If 'w' or 'h' are lower or equal to 0,
// or undefined,
// the constructor creates
// an empty object.

// make it have a 'print' method to it
// that prints the Rectangle instance(s)
// with the character 'X'.

// make it have a 'rotate' method that exchanges
// the Rectangle instances' 'width' and 'height'
// fields.
// --and--
// make it have a 'double' method that multiplies
// the 'width and the 'height' of the Rectangle
// instance(s) by 2.

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined ||
      h <= 0 || h === undefined) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
