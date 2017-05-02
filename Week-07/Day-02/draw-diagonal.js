'use strict';

var lineCount =16;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is


var percent = '';
for (var i = 0; i < lineCount; i++) {
  percent += '%';
}
console.log(percent);

for (var k = 1; k < lineCount-1; k++) {
  var percent2 = '%';
  for (var j = 1; j < k; j++) {
    percent2 += ' ';
  }
  percent2 += '%';
  for (var j = 1; j < lineCount-1-k; j++) {
    percent2 += ' ';
  }
  percent2 += '%';
  console.log(percent2);
}

console.log(percent);
