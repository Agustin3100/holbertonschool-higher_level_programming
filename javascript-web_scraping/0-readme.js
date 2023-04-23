#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
try {
  const data = fs.readFileSync(filePath, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
