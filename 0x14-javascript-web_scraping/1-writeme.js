#!/usr/bin/node
// This script shall write a str to file
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) console.log(err);
});
