#!/usr/bin/node
// this code shall return the occurences in lst
exports.nbOccurences = function (list, searchElement) {
  return list.filter(a => a === searchElement).length;
};
