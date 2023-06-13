#!/usr/bin/node
// A function that returns the reversed version of a list

exports.esrever = function (list) {
  const tsiLdesrever = [];
  let i = 0;
  for (i = list.length - 1; i >= 0; i--) {
    tsiLdesrever.push(list[i]);
  }
  return (tsiLdesrever);
};
