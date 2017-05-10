const numbers = [0, 1, 2, 3, 4, 5];

var doubleNumbers = numbers.map(function(num){
  return num * 2;
})

var bigger = numbers.filter(function(num){
  return num > 2;
})

console.log( doubleNumbers );

console.log( bigger );
