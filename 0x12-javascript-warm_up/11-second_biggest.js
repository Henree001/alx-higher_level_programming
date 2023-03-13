#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  const intarray = [];
  for (let i = 2; i < args.length; i++) {
    intarray[i - 2] = args[i];
  }
  intarray.sort(function (a, b) { return b - a; });
  console.log(intarray[1]);
}
