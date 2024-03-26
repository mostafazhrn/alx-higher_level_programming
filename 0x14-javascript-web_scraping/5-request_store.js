#!/usr/bin/node
// This code shall get webpage content and store it in a file
const req = require('request');
const fs = require('fs');
req(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
