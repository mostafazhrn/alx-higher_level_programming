#!/usr/bin/node
// This code shall print num of args
let x = 0;
exports.logMe = function (item) {
  console.log(x + ': ' + item);
  x++;
};
