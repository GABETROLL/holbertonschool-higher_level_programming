#!/usr/bin/node

// Exercise 8: Make a function that returns
// the reversed version of an array named 'list'.
// using 'list.reverse' is NOT ALLOWED.

exports.esrever = function (list) {
  const result = [];

  for (let index = list.length - 1; index >= 0; index--) {
    result.push(list[index]);
  }

  return result;
};
