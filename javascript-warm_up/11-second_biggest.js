#!/usr/bin/node

// Exercise 10: Print the factorial of the "first"
// shell argument. If the argument is NaN,
// the result is 1.
// It must be calculated recursively, in a function.

const argv = require('process').argv;

const nums = argv.slice(2, undefined);
nums.sort((a, b) => b - a);

let answer = 0;

if (nums.length > 1) {
  answer = nums[1];
}

console.log(answer);
