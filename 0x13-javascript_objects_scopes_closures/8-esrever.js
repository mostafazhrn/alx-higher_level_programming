#!/usr/bin/node
// This code shall return list in reverse
exports.esrever = function (list) {
  const reversed = [];
  for (let x = list.length - 1; x >= 0; x--) {
    reversed.push(list[x]);
  }
  return reversed;
};
