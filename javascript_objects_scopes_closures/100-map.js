#!/usr/bin/node

exports.list = [1, 2, 3, 4, 5];
const newList = list.map((value, index) => value * index);
console.log(list); 
console.log(newList);
