#!/usr/bin/node
const firstArg = process.argv[2];
const size = parseInt(firstArg);


if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(firstArg));
  }
} else {
  console.log('Missing size');
}
