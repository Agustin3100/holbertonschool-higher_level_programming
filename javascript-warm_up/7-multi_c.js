#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  const xvalue = process.argv[2];
  for (let i = 0; i < xvalue; i++) {
    console.log('C is fun');
  }
}
