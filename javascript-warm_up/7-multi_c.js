#!/usr/bin/node

const firstArg = process.argv[2];
const repeatCount = parseInt(firstArg);

if (!isNaN(repeatCount)) {
  for (let i = 0; i < repeatCount; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
