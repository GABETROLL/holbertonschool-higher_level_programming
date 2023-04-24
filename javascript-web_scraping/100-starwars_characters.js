#!/usr/bin/node

/*
Exercise 7: Make a script that prints
all the characters of a Star Wars movie
in this API:
https://swapi-api.hbtn.io/(api/films/<movie id arg>)
where 'movie id arg' is a shell argument
of the movie id (a base-10 natural)
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
