#!/usr/bin/node
// THis code shall print addition of 2 ints
function add (a, b) {
  console.log(a + b);
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
