#!/usr/bin/node
const myObject = {
    type: 'object',
    value: 12
  };
  console.log(myObject);
function incr(x) {
    x = parseInt(x);
    if (isNaN(x)) {
      return 0;
    }
    return x + 1;
  }
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
