#!/usr/bin/node
exports.esrever = function (list) {
  let lgth = list.length - 1;
  let i = 0;
  while ((lgth - i) > 0) {
    const holder = list[lgth];
    list[lgth] = list[i];
    list[i] = holder
    i++;
    lgth--;
  }
  return list;
};
