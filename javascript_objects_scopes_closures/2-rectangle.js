#!/usr/bin/node

// Exercise 1: make an Rectangle class
// with 'width' and 'height' fields,
// and a constructor that takes args 'w' and 'h'
// and assigns 'w' to 'width'
// and 'h' to 'height'.

// If 'w' or 'h' are 0, the constructor creates
// an empty object

class Rectangle {
  constructor (w, h) {
    if (w || h === 0) {
      return;
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
