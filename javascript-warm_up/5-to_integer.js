#!/usr/bin/node

// Exercise 5:
// Print the "first" shell argument
// converted to an integer,
// if it can be converted to an integer.

const process = require('process');
const argv = process.argv;
const argInt = parseInt(argv[2]);

if (isNaN(argInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argInt);
}
