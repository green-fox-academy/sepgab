// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
//

var black = '%';
var white = ' ';

for (i = 0; i < 4; i++) {
  var row1 = ''
  for (j = 0; j < 4; j++) {
    row1 += '% '
  }
  console.log(row1)
  var row2 = ''
  for (j = 0; j < 4; j++) {
    row2 += ' %'
  }
  console.log(row2)
}
