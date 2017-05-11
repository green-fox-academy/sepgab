'use strict';

let main = document.querySelector('main');
let resp = {};
let listOfImages = []

let httpRequest = new XMLHttpRequest();

httpRequest.open('GET', 'http://api.giphy.com/v1/gifs/search?q=javascript&api_key=dc6zaTOxFJmzC', true);

httpRequest.send();

httpRequest.onreadystatechange = function() {
  if (httpRequest.readyState === 4) {
    resp = JSON.parse(httpRequest.response);
    for (let i = 0; i < 16; i++) {
      let imgToAdd = document.createElement('img');
      imgToAdd.setAttribute('src', resp.data[i].images.original_still.url);
      imgToAdd.addEventListener('click', function(){
        imgToAdd.setAttribute('src', resp.data[i].images.original.url);
      });
      main.appendChild(imgToAdd);
    }
  }

}
