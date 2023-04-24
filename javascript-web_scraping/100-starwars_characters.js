#!/usr/bin/node

/*
Exercise 7: Make a script that prints
all the characters of a Star Wars movie
in this API:
https://swapi-api.hbtn.io/(api/films)
*/

const request = require('request');
const { fileURLToPath } = require('url');

const URL = 'https://swapi-api.hbtn.io/api/films';
const movie_id = require('process').argv[2];

request(URL, function (error, response, body) {
	if (error) {
    console.log('error: ' + response);
    return;
  }
  const films = JSON.parse(body).results;
  const film_character_urls = films[movie_id].characters;
  // wrong

  for (const charcter_url of film_character_urls) {

    console.log('character_url: ' + charcter_url);

    request(charcter_url, function (error, response, body) {
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
