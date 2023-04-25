#!/usr/bin/node
/*
Exercise 3: make a script
that prints the number of Star Wars movies
where the character "Wedge Antilles",

whose character URL is
'https://swapi-api.hbtn.io/api/people/18/',
(but we only care about the last part
of the URL: '18/')

is present
from this API: https://swapi-api.hbtn.io/api/films/
which *should* be provided in the only
shell argument for this script.
*/

const process = require('process');
const URL = process.argv[2];

const request = require('request');

request(URL, function (error, response, body) {
  if (error) {
    console.log('error');
  } else {
    const allMovies = JSON.parse(body).results;

    let moviesStarring18 = 0;
    for (movie of allMovies) {
      if (movie.characters.some((item) => item.endsWith('18/'))) {
        moviesStarring18++;
      }
    }
    console.log(moviesStarring18);
  }
});
