#!/usr/bin/node
// This script shall print sq
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  for (let y = 0; y < x; y++) {
    console.log('X'.repeat(x));
  }
}
