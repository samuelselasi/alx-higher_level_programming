#!/usr/bin/node
/* A script that imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence
 */

const dict = require('./101-data.js').dict;
const sortedDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (occurrences in sortedDict) {
    sortedDict[occurrences].push(userId);
  } else {
    sortedDict[occurrences] = [userId];
  }
}
console.log(sortedDict);
