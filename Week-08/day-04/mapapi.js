'use strict';

let button = document.querySelector('button');
let city = document.querySelector('input');
let answer = document.querySelector('div');
let map = document.querySelector('iframe')
let resp = {};


let getLocation = function() {
  let xhr = new XMLHttpRequest();
  let url = 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=' + city.value;

  xhr.open( 'GET', url, true )
  xhr.setRequestHeader('X-Mashape-Key', 'iB02ezuUIEmshbdzZNva7NSnj7vpp1THxLjjsn1KERUHSl0q87');
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.send()

  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      resp = JSON.parse(xhr.response)
      console.log( resp );
      answer.innerText = '\nLatitude: ' + resp.Results[0].lat + ', \n Longitude: ' + resp.Results[0].lon;
      map.setAttribute('src',  'https://www.google.com/maps/embed/v1/place?key=AIzaSyB9gckgAPO99FU6LfsH42pAOKXCuxMgeuA&q=' + city.value)
    }
  }
}



button.addEventListener('click', getLocation)
