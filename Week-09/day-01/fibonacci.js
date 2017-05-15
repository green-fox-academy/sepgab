// Fibonacci
//
// Write a function that computes a member of the fibonacci sequence by a given index
// Create tests that covers all types of input (like in the previous workshop exercise)

'use strict';

let getFibonacci = function(number) {
  if (Number.isInteger(number) && number > 0) {
    if (number < 3) {
      return 1;
    } else {
      return getFibonacci(number-1) + getFibonacci(number-2);
    }
  } else {
    return 'Incorrect input'
  }

}

console.log(getFibonacci(6));

module.exports = {
  getFibonacci: getFibonacci
}
