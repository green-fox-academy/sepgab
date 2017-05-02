'use strict';

// Write a program that prints the numbers from 1 to 100.
// But for multiples of three print “Fizz” instead of the number
// and for the multiples of five print “Buzz”.
// For numbers which are multiples of both three and five print “FizzBuzz”

for (var i = 1; i <= 100; i++) {
  var variant = i;
  if (i % 3 === 0) {
    variant = 'Fizz';
  }
  if (i % 5 === 0) {
    variant = 'Buzz';
  }
  if (i % 3 === 0 && i % 5 === 0) {
    variant = 'FizzBuzz';
  }
  console.log(variant)
}
