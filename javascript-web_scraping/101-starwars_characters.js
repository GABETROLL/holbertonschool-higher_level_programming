#!/usr/bin/node

/*
Exercise 8: Make a script that prints
all the characters of a Star Wars movie
in this API:
https://swapi-api.hbtn.io/(api/films/<movie id arg>)
where 'movie id arg' is a shell argument
of the movie id (a base-10 natural)

BUT in the order they are listed in the JSON response.

TURNS OUT, the 7th exercise here already did the same thing,
so this file is just a copy of the 100 file,
but with this longer comment and 101 instead
*/

const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/';

const movieId = require('process').argv[2];

if (movieId === undefined) {
  throw new Error('Must provide a movie id arg.');
  // This exception
  // always ends the program
  // when no arg is provided.
}

request(URL + movieId, function (error, response, body) {
  if (error) {
    console.log('error: ' + response);
    return;
  }
  const films = JSON.parse(body);

  const filmCharacterUrls = films.characters;

  for (const charcterUrl of filmCharacterUrls) {
    request(charcterUrl, function (error, response, body) {
      if (error) {
        console.log('error: ' + response);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
}
);
