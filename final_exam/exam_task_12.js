//Create a function that takes a matrix (list of lists) of numbers and returns the sum of each rows as an array.

'use strict';

let matrixRowSum = function(listOfLists) {
  let result = [];
  for (let i = 0; i < listOfLists.length; i++) {
    let rowSum = 0;
    for (let j = 0; j < listOfLists[i].length; j++) {
      rowSum += listOfLists[i][j];
    }
    result.push(rowSum);
  }
  return result;
}

console.log(matrixRowSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
