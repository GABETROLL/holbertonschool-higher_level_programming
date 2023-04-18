#!/usr/bin/node

// Exercise 3:
// Print the "first" shell argument
// if there is one.

const process = require('process');
const argv = process.argv;

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
