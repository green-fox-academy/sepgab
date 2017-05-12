'use strict';

let main = document.querySelector('main')
let resp = {}
let xhr = new XMLHttpRequest();

// xhr.open('GET', 'http://10.27.99.59:8080/posts', true);
xhr.open('GET', 'https://time-radish.glitch.me/posts', true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send();

xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    resp = JSON.parse(xhr.response);
    console.log(resp);
    let postLength = resp.posts.length
    console.log(postLength);
    for (let i = 0; i < postLength; i++) {
      let ArtToAdd = document.createElement('article');
      main.appendChild(ArtToAdd);

      let ordinal = document.createElement('div');
      ordinal.className = 'ordinal'
      ordinal.innerText = i+1;
      ArtToAdd.appendChild(ordinal);

      let stat = document.createElement('div');
      stat.className = 'stat';
      ArtToAdd.appendChild(stat);

      let upvote = document.createElement('div');
      upvote.className = 'upvote';
      upvote.addEventListener('click', function(){
        upvote.style.backgroundImage = 'url(css/images/upvoted.png)';
        votes.innerText++;
        voteUpdater();
      });
      stat.appendChild(upvote);

      let votes = document.createElement('div');
      votes.className = 'votes';
      votes.innerText = resp.posts[i].score;
      stat.appendChild(votes);

      let downvote = document.createElement('div');
      downvote.className = 'downvote';
      downvote.addEventListener('click', function(){
        downvote.style.backgroundImage = 'url(css/images/downvoted.png)';
        votes.innerText--;
        voteUpdater();
      });
      stat.appendChild(downvote);

      let post = document.createElement('div');
      post.className = 'post';
      ArtToAdd.appendChild(post);

      let headline = document.createElement('a')
      headline.className = 'headline';
      headline.setAttribute('href', resp.posts[i].href);
      headline.innerText = resp.posts[i].title;
      post.appendChild(headline);

      let infos = document.createElement('div');
      infos.className = 'infos';
      let date = resp.posts[i].timestamp;
      let owner = resp.posts[i].owner
      if (owner === null || typeof owner === 'undefined') {
        owner = 'anonymous';
      }
      infos.innerText = 'Submitted at ' + timeConverter(date) + ' by ' + owner;
      post.appendChild(infos);

      let actions = document.createElement('div');
      actions.className = 'actions';
      post.appendChild(actions);

      let modify = document.createElement('a');
      modify.innerText = 'modify ';
      actions.appendChild(modify);

      let remove = document.createElement('a');
      remove.innerText = 'remove';
      actions.appendChild(remove);
    }
  }
}

let voteUpdater = function() {
  // PUT metódus majd ide jönne...
}

let timeConverter = function(timestamp) {
  var a = new Date(timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var time = date + ' ' + month + ' ' + year + ' ' + hour + ':';
  return time;
}
