#!/usr/bin/node

// Print function with custom characters to represent the Square

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
