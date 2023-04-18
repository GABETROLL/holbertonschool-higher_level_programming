#!/usr/bin/node

// Exercise 13: Make another 'add' function
// that's accessible from outside this file,
// when this file is required from another
// .js file.

exports.add = function (a, b) {
  return a + b;
};
