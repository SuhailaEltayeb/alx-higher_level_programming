#!/usr/bin/node
const dict = require('./101-data').dict;

const alllist = Object.entries(dict);
const _values = Object.values(dict);
const unic_values = [...new Set(_values)];
const newDict = {};
for (const j in unic_values) {
  const list = [];
  for (const k in alllist) {
    if (alllist[k][1] === unic_values[j]) {
      list.unshift(alllist[k][0]);
    }
  }
  newDict[unic_values[j]] = list;
}
console.log(newDict);
