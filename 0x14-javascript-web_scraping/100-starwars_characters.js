#!/usr/bin/node
// This script shall print all characters of star war movie
const req = require('request');
const link = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
req(link, (err, response, body) => {
  if (err) return;
  for (const char of JSON.parse(body).characters) {
    req(char, (err, response, body) => {
      if (err) return;
      console.log(JSON.parse(body).name);
    });
  }
});
