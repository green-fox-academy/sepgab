'use strict';

var lineCount = 4;

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is

for (var i = 1; i <= lineCount; i++) {
  var stars =''
  for (var j = 1; j <= i; j++) {
    stars += '*';
  }
  console.log(stars);
}
