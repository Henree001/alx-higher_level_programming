#!/usr/bin/node
function factorial (b) {
  if (b === 1 || isNaN(b)) {
    return 1;
  }
  return (b * factorial(b - 1));
}
console.log(factorial(parseInt(process.argv[2])));
