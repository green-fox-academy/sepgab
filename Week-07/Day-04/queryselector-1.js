'use strict';

var king = document.getElementById('b325');
console.log( king.innerText );


var conceited = document.getElementsByClassName('b326');
console.log( conceited[0].childNodes[0].nodeValue );

alert ( conceited[0].childNodes[0].nodeValue );


var businessLamp = document.querySelectorAll('.big');

businessLamp.forEach(function(el) {
  console.log( el.innerText );
})

var businessLamp2 = document.getElementsByClassName('big');

for (var i = 0; i < businessLamp2.length; i++) {
  console.log( businessLamp2[i].innerText );
}


var conceitedKing = document.getElementsByClassName('container')[0];

for (var i = 0; i < conceitedKing.children.length; i++) {
  alert ( conceitedKing.children[i].innerText );
}


var noBusiness = document.querySelectorAll('div');

noBusiness.forEach(function(el) {
  console.log( el.innerText );
})


var allBizniss = document.querySelectorAll('p')[0];

alert ( allBizniss.innerText );
