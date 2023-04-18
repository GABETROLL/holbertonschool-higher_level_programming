#!/usr/bin/node

// Exercise 10: Print the factorial of the "first"
// shell argument. If the argument is NaN,
// the result is 1.
// It must be calculated recursively, in a function.

const argv = require('process').argv;

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const argInt = parseInt(argv[2]);

console.log(factorial(argInt));
