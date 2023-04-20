#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;

const fileName = argv[2];
const content = argv[3];

fs.writeFile(fileName, content, err => {
  if (err) {
    console.error(err);
  }
  // file written successfully
}
);
