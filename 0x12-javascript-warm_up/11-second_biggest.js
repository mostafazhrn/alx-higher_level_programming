#!/usr/bin/node
// This script shall search the 2nd big int
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const x = process.argv.slice(2);
  x.sort(function (a, b) { return a - b; });
  console.log(x[x.length - 2]);
}
