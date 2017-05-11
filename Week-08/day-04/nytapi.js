'use strict';

let list = document.querySelector('div');
let resp = {};
let listOfArticles = {};

let url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
url += "?q=" + "moon landing by Apollo 11" + "&api_key=" + "10c8315ca04b48a3b091477a3e56201c"

let httpRequest = new XMLHttpRequest();

httpRequest.open('GET', url, true);

httpRequest.send();

httpRequest.onreadystatechange = function() {
  if (httpRequest.readyState === 4) {
    resp = JSON.parse(httpRequest.response);
    for (let i = 0; i < resp.response.docs.length; i++) {
      let headline = document.createElement('a')
      headline.innerText = resp.response.docs[i].headline.main;
      headline.setAttribute('href', resp.response.docs[i].web_url);
      let artToAdd = document.createElement('article');
      artToAdd.innerText = resp.response.docs[i].snippet + '\n' + resp.response.docs[i].pub_date + '\n \n';
      list.appendChild(headline);
      list.appendChild(artToAdd);
    }
  }
}
