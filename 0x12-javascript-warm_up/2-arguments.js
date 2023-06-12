#!/usr/bin/node
/* A script that prints a message depending of the number of arguments passed:
 * If no arguments are passed to the script, print “No argument”
 * If only one argument is passed to the script, print “Argument found”
 * Otherwise, print “Arguments found”
 */

const args = process.argv.length;
if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
