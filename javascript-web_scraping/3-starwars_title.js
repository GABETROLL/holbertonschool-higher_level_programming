#!/usr/bin/node
/*
Exercise 3: make a script
that prints the title of a Star Wars movie
from this API: https://swapi-api.hbtn.io/api/films/:id
taking in an 'id' shell argument
*/

const URL = 'https://swapi-api.hbtn.io/api/films/';
const id = require('process').argv[2];
const request = require('request');

request(URL + id, function (error, response, body) {
  if (error) {
    console.log('invalid Star Wars movie ID: ' + id);
  } else {
    console.log(body);
    // the API returns the move title in the body
  }
});
