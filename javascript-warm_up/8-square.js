#!/usr/bin/node
const firstArg = process.argv[2];
const size = parseInt(firstArg);


if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    var row = "";
    for (let j = 0; j < size; j++) {
      row += "#";
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
