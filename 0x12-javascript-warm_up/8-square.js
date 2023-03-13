#!/usr/bin/node
const args = process.argv;
const X = parseInt(args[2]);
let i;
if (isNaN(X)) {
  console.log('Missing size');
} else {
  for (i = 0; i < X; i++) {
    console.log('X'.repeat(X));
  }
}
