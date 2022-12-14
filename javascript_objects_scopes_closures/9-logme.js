#!/usr/bin/node

let count = 0;
exports.logMe = function(item) {
    // keep track of the number of arguments printed
    console.log(`${count++}: ${item}`);
  }
