#!/usr/bin/node

// Exercise 5: Make a Square class that inherits
// from the Rectangle class in exercise 4
// and initializes its sides to a constructor argument,
// 'size', using 'super'.

const Rectangle = require('4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
