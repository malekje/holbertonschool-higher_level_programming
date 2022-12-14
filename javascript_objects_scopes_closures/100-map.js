#!/usr/bin/node

const initialList = [1, 2, 3, 4, 5];
const newList = initialList.map((value, index) => value * index);
// Print the initial and new arrays
console.log(initialList); 
console.log(newList);
