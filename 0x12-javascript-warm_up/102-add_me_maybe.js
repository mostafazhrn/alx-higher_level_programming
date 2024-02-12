#!/usr/bin/node
// THis code shall inc and call func
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
