'use strict';

console.log('Majom');

function greet(name) {
  console.log('Hello ' + name);
}

greet('Joci');

var koszonesi = greet;

koszonesi('Pako');

greet.robika = 4;
console.log(greet.robika);

var anonymous = function() {
  console.log('Marpedig en vagyok a fuggveny a nev nelkul!');
};

anonymous();

(function () {
  var kecske = 4;
  console.log('Egy masik nev nelkuli fuggveny, akit nem lehet újra meghívni, soha többé - akiből nem látszik ki a kecske sem');
  console.log(kecske);
})();
