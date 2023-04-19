#!/usr/bin/node

// Exercise 10: make a function that converts
// a number into its string representation
// with base N.

// The function must be used like this:
// c = converter(<base>);
// strResult = c(<number>);

exports.converter = function (base) {
  return ((number) => number.toString(base));
}
