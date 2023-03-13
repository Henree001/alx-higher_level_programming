#!/usr/bin/node
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return (a + b);
}
if (process.argv.length <= 3) {
  console.log('NaN');
} else {
  const sum = add(process.argv[2], process.argv[3]);
  console.log(sum);
}
