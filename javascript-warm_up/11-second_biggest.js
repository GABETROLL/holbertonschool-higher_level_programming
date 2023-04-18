#!/usr/bin/node

// Exercise 10: Print the factorial of the "first"
// shell argument. If the argument is NaN,
// the result is 1.
// It must be calculated recursively, in a function.

const argv = require('process').argv;

let biggest = undefined;

for (const index of argv) {
  if (index < 2) {
    continue;
  }

  const argInt = parseInt(argv[index]);
  if (isNaN(argInt)) {
    continue;
  }

  if (biggest === undefined || argInt > biggest) {
    biggest = argInt;
  }
}

if (biggest === undefined) {
  biggest = 0;
}

console.log(biggest);
