#!/usr/bin/node
let argument;
if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  argument = process.argv[2];
  console.log(argument);
}
