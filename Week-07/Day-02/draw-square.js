'use strict';

var lineCount = 15;

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

var percent = '';
for (var i = 1; i < lineCount; i++) {
  percent += '%';
}
console.log(percent);

var percent2 = '%';
for (var j = 1; j < lineCount-2; j++) {
  percent2 += ' ';
}
percent2 += '%';

for (var k = 1; k < lineCount-1; k++) {
  console.log(percent2);
}

console.log(percent);
