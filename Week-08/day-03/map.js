'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

let eOccurs = fruits.map(function(fruit) {
  let e = 0;
  for (let i = 0; i < fruit.length; i++) {
    if (fruit[i] === 'e') {
      e++;
    }
  }
  return e;
})

console.log( eOccurs );
