#!/usr/bin/node

/*
Exercise 5: make a script that GETs the content
of a webpage and stores it in a file.

Both the URL and the file are shell arguments,
in that order.
*/

const request = require('request');

const argv = require('process').argv;
const URL = argv[2];
const outputFile = argv[3];

const fs = require('fs');

request(URL, function (error, response, body) {
    if (error) {
        console.log('error requesting: ' + response);
        return;
    }
    fs.writeFile(outputFile, body, error => {
        if (error) {
            console.error(error);
        }
        // file written successfully
    }
    );
}
);


