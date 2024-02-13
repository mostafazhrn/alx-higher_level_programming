#!/usr/bin/node
// This code shall convert num from base 10 to other base
// passed as arg
exports.converter = function (base) {
  return number => number.toString(base);
};
