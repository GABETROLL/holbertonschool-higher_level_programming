#!/usr/bin/node
/*
Exercise 2: make a script
that takes in a URL as an argument
and outputs the status code of the
'GET' request to that URL.
*/

const URL = require('process').argv[2];
const request = require('request');

request(URL, function (error, response, body) {
    console.log(response.statusCode);
});
