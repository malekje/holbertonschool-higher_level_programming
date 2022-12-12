#!/usr/bin/node

module.exports = class Square extends require('./4-rectangle.js') {
  constructor(size) {
    // Call the constructor of the superclass (Rectangle)
    // with the size argument as both the width and height
    super(size, size);
  }
};
