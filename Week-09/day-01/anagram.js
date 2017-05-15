'use strict'

// Anagram
//
// Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
// Create a test for that.

let anagramChecker = function(string) {
  return string === string.split('').reverse().join('');
}

module.exports = {
  anagramChecker: anagramChecker
}
