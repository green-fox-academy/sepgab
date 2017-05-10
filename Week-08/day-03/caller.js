'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
}

function selectLastEvenNumber(list, callback) {
  let lastEvenNumber = -1
  while (lastEvenNumber === -1) {
    let removed = list.splice(list.length - 1, 1);
    if (removed % 2 === 0) {
      lastEvenNumber = removed;
    }
  }
  return callback(lastEvenNumber);
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8
