#!/usr/bin/node

/*
Exercise 6: make a script that computes
the number of tasks completed by user id
from the first shell argument,
assuming that it's this API:
https://jsonplaceholder.typicode.com/todos
*/

const request = require('request');

const argv = require('process').argv;
const API = argv[2];

request(API, function (error, response, body) {
  if (error) {
    console.log('error: ' + response);
    return;
  }

  const tasks = JSON.parse(body);

  const usersAndTasks = {};

  for (const task of tasks) {
    if (task.completed) {
      if (usersAndTasks[task.userId] === undefined) {
        usersAndTasks[task.userId] = 1;
      } else {
        usersAndTasks[task.userId]++;
      }
    }
  }

  console.log(usersAndTasks);
}
);
