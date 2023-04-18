#!/usr/bin/node

// Exercise 4:
// Print the "first two" shell arguments
// like this:
// "<arg 1> is <arg 2>"

const process = require('process');
const argv = process.argv;

console.log(argv[2] + ' is ' + argv[3]);
