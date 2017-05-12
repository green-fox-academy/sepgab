'use strict';

let button = document.querySelector('button');
let sentence = document.querySelector('input');
let sentence2 = '';
let answer = document.querySelector('div');
let resp = {};



let getYoda = function() {
  sentence2 = sentence.value.split(' ').join('+')
  let xhr = new XMLHttpRequest();
  let url = 'https://yoda.p.mashape.com/yoda?sentence=' + sentence2;
  xhr.open( 'GET', url, true )
  xhr.setRequestHeader('X-Mashape-Key', 'iB02ezuUIEmshbdzZNva7NSnj7vpp1THxLjjsn1KERUHSl0q87');
  xhr.setRequestHeader('Accept', 'text/plain');
  xhr.send()
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      answer.innerText = xhr.response;
    }
  }
}

button.addEventListener('click', getYoda)
