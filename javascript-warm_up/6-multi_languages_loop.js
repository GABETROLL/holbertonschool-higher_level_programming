#!/usr/bin/node

// Exercise 6: Print messages by iterating
// through an array, and using "console.log"
// ONLY ONCE.
// (except the first 2 in the argv array)

const argv = require('process').argv;

for (index = 2; index < argv.length; index++) {
  console.log(argv[index]);
}
