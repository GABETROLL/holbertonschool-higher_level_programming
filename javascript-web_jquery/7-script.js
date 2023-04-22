#!/usr/bin/node

// Exercise 7:
// Select 'DIV#character'
// and replace its content
// with the character 'name' from this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
// ... all done with jquery and plain JavaScript.

const character_div = $('DIV#character');

$.get(
    'https://swapi-api.hbtn.io/api/people/5/?format=json',
    function (character_data, status) {
        character_div.html(character_data.name);
    }
);
