'use strict';

console.log('Alma');

var a = 23;

if (a === 123) {
  console.log('YEEEY');
} else if a === 23) {
  var b = 11;
  console.log('Not so YEEEY');
} else {
  console.log('kacsa');
}

console.log(b);

var i = 0
while(i < 10) {
  i++;
  console.log(i);
}

for (var i = 0; i < 10; i++) {
  console.log(i);
}


function greet() {
  console.log('Majom')
}

greet();

function returnTrue() {
  console.log('lefut');
  return true
}

returnTrue()

var i = 10;
while (i) { console.log(i--); }
