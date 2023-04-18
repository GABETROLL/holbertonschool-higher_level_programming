#!/usr/bin/node

// Exercise 4: make an Rectangle class
// with 'width' and 'height' fields,
// and a constructor that takes args 'w' and 'h'
// and assigns 'w' to 'width'
// and 'h' to 'height'.

// If 'w' or 'h' are lower or equal to 0,
// or undefined,
// the constructor creates
// an empty object.

// make it have a 'print' method to it
// that prints the Rectangle instance
// with the character 'X'.
// --and---


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
}

module.exports = Rectangle;
