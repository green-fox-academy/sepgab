'use strict';

var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for (var i = 1; i <= lineCount; i++) {
  var stars =''
  for (var j = lineCount-i; j > 0; j--) {
    stars += ' ';
  }
  for (var j = 1; j <= 2*i-1; j++) {
    stars += '*';
  }
  console.log(stars);
}
