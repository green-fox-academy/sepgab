'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

let pearPrinter = function() {
  console.log('pear');
}

let melonPrinter = function() {
  console.log('melon');
}

let grapesPrinter = function() {
  console.log('grapes');
}

console.log('apple');
setTimeout(pearPrinter, 1000);
setTimeout(melonPrinter, 3000);
setTimeout(grapesPrinter, 5000);
