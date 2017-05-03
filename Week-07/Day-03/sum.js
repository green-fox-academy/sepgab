'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function summer(number) {
  var result = 0
  for (var i = 1; i <= number; i++) {
    result += i;
  }
  return result;
}

console.log( summer(10) );
