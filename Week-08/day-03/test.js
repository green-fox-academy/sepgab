const numbers = [0, 1, 2, 3, 4, 5];

var doubleNumbers = numbers.map(function(num){
  return num * 2;
})

var bigger = numbers.filter(function(num){
  return num > 2;
})

console.log( doubleNumbers );

console.log( bigger );


// asynchronity

function greet1() {
  console.log('hi!');
}

function greet2() {
  console.log('hello!');
}

function greet3() {
  console.log('waazup!');
}

greet1();
setTimeout(greet2, 1000);
greet3();


function greet4() {
  console.log('hi!');
}

function greet5(anything) {
  anything();
}

function greet6() {
  console.log('HEHE!');
}

greet5(greet4);


function substract(a, b) {
  return a - b;
}

substract.pear = 45;
console.log(substract.pear);
