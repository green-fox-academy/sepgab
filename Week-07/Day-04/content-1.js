'use strict'

var heading = document.querySelector('h1');

alert ( heading.innerText );


var firstPar = document.querySelector('p');

console.log ( firstPar.innerText );


var secondPar = document.querySelector('.other');

alert ( secondPar.innerText );


heading.innerText = 'New content';


var thirdPar = document.querySelector('.result');

thirdPar.innerText = firstPar.innerText;
