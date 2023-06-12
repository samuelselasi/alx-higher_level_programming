#!/usr/bin/node
// A function that executes x times a function

exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  for (i = 0; i < x; i++) theFunction();
};
