'use strict';

var lineCount = 15;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

for (var i = 1; i <= lineCount/2+1; i++) {
  var stars =''
  for (var j = lineCount-i; j > lineCount/2; j--) {
    stars += ' ';
  }
  for (var j = 1; j <= 2*i-1; j++) {
    stars += '*';
  }
  console.log(stars);
}

for (var i = 1; i <= lineCount/2; i++) {
  var stars =''
  for (var j = 0; j < i; j++) {
    stars += ' ';
  }
  for (var j = 0; j < lineCount-2*i; j++) {
    stars += '*';
  }
  console.log(stars);
}
