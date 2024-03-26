#!/usr/bin/node
// THis cpde shall read and print the content of file
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  console.log(err || data);
});
