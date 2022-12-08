#!/usr/bin/node
const firstArg = process.argv[2];
const secondArg = process.argv[3];

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

  console.log(add(firstArg, secondArg));
