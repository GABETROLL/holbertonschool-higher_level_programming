#!/usr/nin/node

// Exercise 8: fetch and listall the the titles
// of all the Star Wars movies from this URL:
// https://swapi-api.hbtn.io/api/films/?format=json,
// and list them inside
// a UL tag with id='list_movies'
// only using jquery and ajax.

const movies_list = $('UL#list_movies');

$.get(
    'https://swapi-api.hbtn.io/api/films/?format=json',
    function (movies_data_JSON, status) {
        const movies_JSON = movies_data_JSON.results;

        for (const movie_JSON of movies_JSON) {
            movies_list.append('<li>' + movie_JSON.title + '</li>');
        }
    }
);
