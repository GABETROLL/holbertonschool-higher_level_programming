#!/usr/bin/node
/*
Exercise 3: make a script
that prints the number of Star Wars movies
where the character "Wedge Antilles"
is present
from this API: https://swapi-api.hbtn.io/api/people/18
(The character has 18 is its ID)
*/

const URL = 'https://swapi-api.hbtn.io/api/people/18';
const request = require('request');

request(URL, function (error, response, body) {
  if (error) {
    console.log('error');
  } else {
    const moviesStarring18 = JSON.parse(body).films.length;
    console.log(moviesStarring18);
  }
});
