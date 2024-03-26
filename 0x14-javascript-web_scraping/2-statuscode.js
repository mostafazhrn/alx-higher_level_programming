#!/usr/bin/node
// This code shall display the status code of a GET request
const req = require('request');
req(process.argv[2], (err, response) => {
  console.log(err || `code: ${response.statusCode}`);
});
