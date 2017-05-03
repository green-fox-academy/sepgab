'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(number) {
  var result = 1
  for (var i = 1; i <= number; i++) {
    result *= i;
  }
  return result;
}

console.log( factorio(6) );
