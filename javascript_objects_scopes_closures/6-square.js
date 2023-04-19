#!/usr/bin/node

// Exercise 6: Define a new class named 'Square'
// that INHERITS FROM the 'Square' class IN THE
// '5-square.js' file.

// Add a new method to it that prints the square
// with a specific character 'c'. If that character
// is undefined, use 'X'.

const Square = require('./5-square');

class Square extends Square {
    charPrint(c) {
        if (c === undefined) {
            c = 'X';
        }
        for (let h = 0; h < this.height; h++) {
            console.log('X'.repeat(this.w));
            // 'h' and 'w' should be the same anyways,
            // and I feel like this is an error-prone
            // way to implement this, but there isn't
            // a 'size' getter here...
        }
    }
}

module.exports = Square;
