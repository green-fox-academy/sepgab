'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

var rows = 10;

for (var i = 1; i <= rows; i++) {
  var line = '';
  for (var j = 0; j < rows; j++) {
    if (j === rows-i) {
      line += ' 1'
    } else {
      line += ' 0'
    }
  }
  console.log( line );
}
