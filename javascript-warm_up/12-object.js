#!/usr/bin/node

// Exercise 12: Change the object's
// '12' to an '89'. (at run-time)

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.value = 89;

console.log(myObject);
  