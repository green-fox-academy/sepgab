//Create a function that takes two strings and returns an array of characters that consitst all the common letters of the two arrays.

'use strict';

let commonStringFinder = function(string1, string2) {
  let result = [];
  for (let i = 0; i < string1.length; i++) {
    for (let j = 0; j < string2.length; j++) {
      if (string2[j] === string1[i] && result.indexOf(string2[j]) === -1 ) {
        result.push(string2[j]);
      }
    }
  }
  return result;
}

console.log(commonStringFinder('Alma Ata', 'Latabár Aladár'));
