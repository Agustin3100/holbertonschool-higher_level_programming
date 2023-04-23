#!/usr/bin/node
let argument;
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  argument = process.argv[2];
  console.log(argument);
}
