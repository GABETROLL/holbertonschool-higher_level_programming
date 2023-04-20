#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;

fs.readFile(argv[0], 'utf-8');
