'use strict';

let postUrl = document.querySelector('.field_url');
let postTitle = document.querySelector('.field_title')
let checkbox = document.querySelector('.checkbox')
let button = document.querySelector('.action')


console.log(checkbox);

let createPost = function() {
  let xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://time-radish.glitch.me/posts', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.setRequestHeader('Accept', 'application/json');
  let message = {
    "title": postTitle.value,
    "href": postUrl.value
  }
  xhr.send(JSON.stringify(message));
}

button.addEventListener('click', createPost);
