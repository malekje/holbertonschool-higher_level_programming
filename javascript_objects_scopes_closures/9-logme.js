#!/usr/bin/node

exports.logMe = function(item) {
    // keep track of the number of arguments printed
    if (!this.count) this.count = 0;
    this.count++;
    console.log(`${this.count}: ${item}`);
  }
