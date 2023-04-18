#!/usr/bin/node

// Exercise 1: make an Rectangle class
// with 'width' and 'height' fields,
// and a constructor that takes 'w' and 'h'
// and assigns them to 'widht' and 'height'
// (in that order).

class Rectangle {
    constructor (w, h) {
        this.width = w;
        this.height = h;
    }
}

module.exports = Rectangle;
