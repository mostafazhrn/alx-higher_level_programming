#!/usr/bin/node
// This code shall print star wars episode title
const req = require('request');
const link = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
req(link, (err, response, body) => {
  console.log(err || JSON.parse(body).title);
});
