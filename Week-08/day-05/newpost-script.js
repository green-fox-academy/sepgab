'use strict';

let button = document.querySelector('.action')

let createPost = function() {
  let postUrl = document.querySelector('.field_url');
  let postTitle = document.querySelector('.field_title')
  let checkbox = document.querySelector('.checkbox')
  let xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://localhost:3000/posts', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.setRequestHeader('Accept', 'application/json');
  let message = {
    "title": postTitle.value,
    "href": postUrl.value
  }
  console.log( 'message sent: ' + JSON.stringify(message) );
  xhr.send(JSON.stringify(message));
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      window.location.href = "index.html";
    }
  }
}

button.addEventListener('click', createPost);
