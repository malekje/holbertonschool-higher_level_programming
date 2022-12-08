#!/usr/bin/node

exports.addit = function (number, theFunction) {
    number++;
    theFunction(number);
  };
