// Count Letters
//
// Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.
// Create a test for that.

'use strict';

let letterCounter = function(string) {
  let answer = {};
  let stringArray = string.toString().split('')
  stringArray.forEach(function(el) {
    if (answer[el]) {
      answer[el]++
    } else {
      answer[el] = 1;
    }
  })
  return answer
}

console.log( letterCounter('stringing in the rain') );

module.exports = {
  letterCounter: letterCounter
}
