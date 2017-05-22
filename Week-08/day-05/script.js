'use strict';

var main = document.querySelector('main')
var resp = {}
var xhr = new XMLHttpRequest();

// xhr.open('GET', 'http://10.27.99.59:8080/posts', true);

var getPosts = function() {
  xhr.open('GET', 'http://localhost:3000/posts', true);
  // xhr.open('GET', 'https://time-radish.glitch.me/posts', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      displayPosts()
    }
  }
}

var displayPosts = function() {
  main.innerHTML = '';
  resp = JSON.parse(xhr.response);
  console.log(resp);
  var postLength = resp.posts.length
  console.log(postLength);
  for (var i = 0; i < postLength; i++) {
    var ArtToAdd = document.createElement('article');
    main.appendChild(ArtToAdd);

    var ordinal = document.createElement('div');
    ordinal.className = 'ordinal'
    ordinal.innerText = i+1;
    ArtToAdd.appendChild(ordinal);

    var stat = document.createElement('div');
    stat.className = 'stat';
    ArtToAdd.appendChild(stat);

    var upvote = document.createElement('div');
    upvote.className = 'upvote';
    upvote.addEventListener('click', function(){
      upvote.style.backgroundImage = 'url(css/images/upvoted.png)';
      votes.innerText++;
      voteUp(i);
    });
    stat.appendChild(upvote);

    var votes = document.createElement('div');
    votes.className = 'votes';
    votes.innerText = resp.posts[i].score;
    stat.appendChild(votes);

    var downvote = document.createElement('div');
    downvote.className = 'downvote';
    downvote.addEventListener('click', function(){
      downvote.style.backgroundImage = 'url(css/images/downvoted.png)';
      votes.innerText--;
      voteDown(i);
    });
    stat.appendChild(downvote);

    var post = document.createElement('div');
    post.className = 'post';
    ArtToAdd.appendChild(post);

    var headline = document.createElement('a')
    headline.className = 'headline';
    headline.setAttribute('href', 'http://' + resp.posts[i].href);
    headline.innerText = resp.posts[i].title;
    post.appendChild(headline);

    var infos = document.createElement('div');
    infos.className = 'infos';
    var date = resp.posts[i].timestamp.slice(0, -8);
    var owner = resp.posts[i].owner
    if (owner === null || typeof owner === 'undefined') {
      owner = 'anonymous';
    }
    infos.innerText = 'Submitted at ' + date + ' by ' + owner;
    post.appendChild(infos);

    var actions = document.createElement('div');
    actions.className = 'actions';
    post.appendChild(actions);

    var modify = document.createElement('div');
    modify.innerText = 'modify ';
    modify.addEventListener('click', function(){
      window.location.href = "modifypost.html#" + i;
    });
    actions.appendChild(modify);

    var remove = document.createElement('div');
    remove.innerText = ' remove';
    remove.addEventListener('click', function(){
      removePost(i)
    });
    actions.appendChild(remove);
  }
}

var voteUp = function(num) {
  xhr.open('PUT', 'https://time-radish.glitch.me/posts/' + resp.posts[num].id + '/upvote', true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      getPosts();
    }
  }
}

var voteDown = function(num) {
  xhr.open('PUT', 'https://time-radish.glitch.me/posts/' + resp.posts[num].id + '/downvote', true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      getPosts();
    }
  }
}

var removePost = function(num) {
  xhr.open('DELETE', 'https://time-radish.glitch.me/posts/' + resp.posts[num].id, true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      getPosts();
    }
  }
}



var timeConverter = function(timestamp) {
  var a = new Date(timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var time = date + ' ' + month + ' ' + year + ' ' + hour + ':';
  return time;
}

getPosts();
