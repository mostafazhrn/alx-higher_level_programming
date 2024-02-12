#!/usr/bin/node
// This script shall print c is fun by x
const x = parseInt(process.argv[2]);
if (x) {
  for (let y = 0; y < x; y++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
