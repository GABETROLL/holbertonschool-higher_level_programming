#!/usr/bin/node

// Exercise 7: make a function that returns
// the amount of times a 'searchElement' occurs
// in a list 'list', called 'nbOccurences'.

exports.nbOccurences = function (list, searchEvent) {
  let result = 0;

  for (const item of list) {
    if (item === searchEvent) {
      result++;
    }
  }

  return result;
};
