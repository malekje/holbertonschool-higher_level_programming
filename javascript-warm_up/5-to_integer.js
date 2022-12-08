#!/usr/bin/node

const firstArg = process.argv[2];
const firstArgInt = parseInt(firstArg);

if (!isNaN(firstArgInt)) {
  console.log("My number: " + firstArgInt);
} else {

  console.log('Not a number');
}
