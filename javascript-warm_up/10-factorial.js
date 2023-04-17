#!/usr/bin/node

function factorial (n) {
  let X = parseInt(n);

  if (X <= 0) {
    X = 1;
  } else {
    X = X * factorial(n - 1);
  }
  return X;
}

const res = factorial(process.argv[2]);
console.log(res);
