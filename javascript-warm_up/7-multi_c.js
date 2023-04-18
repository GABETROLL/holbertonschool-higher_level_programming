#!/usr/bin/node

// Exercise 7: Print 'C is fun'
// for the amount of times the "first" shell
// argument says.

// If the argument is not a number or is missing,
// print 'Missing number of occurences'.

argv = require('process').argv;

const occurences = Number(argv[2]);

if (isNaN(occurences) || argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}

