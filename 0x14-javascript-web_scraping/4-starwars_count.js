#!/usr/bin/node
// This code shall print num of movies where wedge antilles present
const req = require('request');
req(process.argv[2], (err, response, body) => {
  if (err) return;
  let compte = 0;
  for (const film of JSON.parse(body).results) {
    for (const char of film.characters) {
      if (char.includes('18')) {
        compte++;
        break;
      }
    }
  }
  console.log(compte);
});
