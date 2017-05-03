'use strict';

var beka = 1;

function hello(name='MySchool') {
  console.log(beka);
  beka = name;
  return name + ' => ' + name;
}
hello('Tibi');
console.log( beka );
