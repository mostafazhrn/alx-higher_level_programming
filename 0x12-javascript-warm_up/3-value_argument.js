#!/usr/bin/node
// This script shall print 1st arg passed
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
