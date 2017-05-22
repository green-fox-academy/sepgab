'use strict';

let postUrl = document.querySelector('.field_url');
let postTitle = document.querySelector('.field_title')
let checkbox = document.querySelector('.checkbox')
let button = document.querySelector('.action')


console.log(checkbox);

let modifyPost = function() {
  let xhr = new XMLHttpRequest();
  let id = window.location.hash;
  xhr.open('PUT', 'https://time-radish.glitch.me/posts/' + id, true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.setRequestHeader('Content-Type', 'application/json');
  let message = {
    "title": postTitle.value,
    "href": postUrl.value
  }
  xhr.send(JSON.stringify(message));;
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      window.location.href = "index.html";
    }
  }
}

button.addEventListener('click', modifyPost);
