'use strict'

var texts = document.getElementsByTagName('p');

var textToFill = document.getElementsByClassName('dog')[0];

for (var i = 0; i < texts.length; i++) {
  texts[i].innerText = textToFill.innerText;
}
