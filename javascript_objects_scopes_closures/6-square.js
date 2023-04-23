#!/usr/bin/node
const rect = require('./5-square');

module.exports = class Square extends rect {
  charPrint (c) {
    let pC;
    if (c) {
      pC = c;
    } else {
      pC = 'X';
    }
    for (let y = 0; y < this.height; y++) {
      console.log(pC.repeat(this.width));
    }
  }
};
