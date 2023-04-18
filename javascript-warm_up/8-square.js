#!/usr/bin/node

// Exercise 8: If the "first" shell argument
// is a valid int,
// print a square made of 'X's
// with side lengths as the first shell argument.
// If the first shell argument isn't a number,
// print 'Missing size'.

const argv = require('process').argv;

const size = Number(argv[2]);

if (isNaN(size) || argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    console.log('X'.repeat(size));
  }
}
