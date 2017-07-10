//Create a function that takes a list of numbers and returns the second biggest element from it.

'use strict';

let secondBiggestFinder = function(listOfNumbers) {
  let biggestNo = null;
  let secondBiggestNo = null;
  for (let i = 0; i < listOfNumbers.length; i++) {
    if (listOfNumbers[i] > biggestNo) {
      secondBiggestNo = biggestNo;
      biggestNo = listOfNumbers[i];
    } else if (listOfNumbers[i] > secondBiggestNo) {
      secondBiggestNo = listOfNumbers[i];
    }
  }
  return secondBiggestNo;
}

console.log(secondBiggestFinder([1, 10, 20, 65, 21, 3, -4, 100, 4.5, 0]));
