#!/usr/bin/node
// This code shall define class square
module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
};
