#!/usr/bin/node

// Exercise 9: Write a function
// that prints the number of arguments
// already printed by it
// and the new argument value

let times = 0;

exports.logMe = function (item) {
  console.log(times + ': ' + item);
  times++;
};
