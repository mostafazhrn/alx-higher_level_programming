#!/usr/bin/node
// THis script shall import array and compute new one
const list = require('./100-data').list;
console.log(list);
console.log(list.map((j, ind) => j * ind));
