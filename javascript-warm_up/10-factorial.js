#!/usr/bin/node
const firstArg = process.argv[2];
const num = parseInt(firstArg);

function factorial (n) {
    if ((isNaN(n)) || (n === 1)) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  console.log(factorial(num));
