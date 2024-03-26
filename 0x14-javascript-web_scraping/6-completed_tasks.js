#!/usr/bin/node
// This code shall compute num of tasks done by user id
const req = require('request');
req(process.argv[2], (err, response, body) => {
  if (err) return;
  const lst = {};
  for (const tache of JSON.parse(body)) {
    if (tache.completed) {
      if (lst[tache.userId] === undefined) {
        lst[tache.userId] = 1;
      } else {
        lst[tache.userId]++;
      }
    }
  }
  console.log(lst);
});
