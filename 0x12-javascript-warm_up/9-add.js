#!/usr/bin/node
function add (a, b) {
  const _sum = a + b;
  console.log(_sum);
}

add(Number(process.argv[2]), Number(process.argv[3]));
