#!/usr/bin/node
const dict = require('./101-data').dict;

const A = Object.entries(dict);
const V = Object.values(dict);
const valsUniq = [...new Set(V)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in A) {
    if (A[k][1] === valsUniq[j]) {
      list.unshift(A[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
