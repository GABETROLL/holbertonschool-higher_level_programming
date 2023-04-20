#!/usr/bin/node

const fs = require('fs');
const inputFile = require('process').argv[2];

if (inputFile !== undefined) {
  fs.readFile(inputFile, 'utf-8',
    function (error, data) {
      if (error) {
        console.log(error);
      } else {
        console.log(data);
      }
    }
  );
}
