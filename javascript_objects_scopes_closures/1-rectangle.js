#!/usr/bin/node

// Exercise 1: make an Rectangle class
// with 'width' and 'height' fields,
// and a constructor that takes args 'w' and 'h'
// and assigns 'w' to 'width'
// and 'h' to 'height'.

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
