#!/usr/bin/node

// Exercise 9: add the "first two" shell arguments
// with an 'add' function and print it out.
// Don't care if the args are undefined.

const argv = require('process').argv;

function add(a, b) {
  return a + b;
}

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

console.log(add(a, b));