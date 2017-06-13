'use strict';

const root = 'http://localhost:3000'

const addPlaylist = document.querySelector('.addPlaylist');
const addPlaylistDialog = document.querySelector('.addPlaylistDialog');
const listOfPlaylists = document.querySelector('.listOfPlaylists');
const playlist0 = document.querySelector('.listOfPlaylists p')
const listOfTracks = document.querySelector('.listOfTracks');
const rewind = document.querySelector('.rewind');
const pause = document.querySelector('.pause');
const forward = document.querySelector('.forward');
const shuffle = document.querySelector('.shuffle');
const addTrack = document.querySelector('.addTrack');
const addTrackDialog = document.querySelector('.addTrackDialog');
const select = document.querySelector('.select');
const addToFav = document.querySelector('.addToFav');
const addToFavStar = document.querySelector('.addToFav img');
const audio = document.querySelector('audio');
const trackTitle = document.querySelector('.trackTitle');
const artist = document.querySelector('.artist');

const cancelButtons = document.querySelectorAll('.cancel');
const submitPlaylistButton = document.querySelector('.submitPlaylist');
const submitTrackButton = document.querySelector('.submitTrack');

let tracksOfActivePlaylist = [];
let idOfActiveTrack = 0;

const ajaxGet = function(url, callback) {
	var xhr = new XMLHttpRequest(),
  method = "GET";

	xhr.open(method, root+url, true);

	xhr.onreadystatechange = function () {
		if(xhr.readyState === XMLHttpRequest.DONE) {
			if(xhr.status === 200) {
				var rsp = JSON.parse( xhr.response );
				callback(rsp);
			} else {
				new Error('API error!');
				console.log(xhr.status);
			}
		}
	};
	xhr.send();
}

const ajaxPost = function(message, url, callback) {
	var xhr = new XMLHttpRequest(),
  method = "POST";

	xhr.open(method, root+url, true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');

	console.log( 'message sent: ' + JSON.stringify(message) );
	xhr.send(JSON.stringify(message));

	xhr.onreadystatechange = function () {
		if(xhr.readyState === XMLHttpRequest.DONE) {
			if(xhr.status === 200) {
				var rsp = JSON.parse( xhr.response );
				callback(rsp);
			} else {
				new Error('API error!');
				console.log(xhr.status);
			}
		}
	};
}

const ajaxPut = function(message, url) {
	var xhr = new XMLHttpRequest(),
  method = "PUT";

	xhr.open(method, root+url, true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');

	console.log( 'message sent: ' + JSON.stringify(message) );
	xhr.send(JSON.stringify(message));

	xhr.onreadystatechange = function () {
		if(xhr.readyState === XMLHttpRequest.DONE) {
			if(xhr.status === 200) {
				var rsp = JSON.parse( xhr.response );
				console.log(rsp);
			} else {
				new Error('API error!');
				console.log(xhr.status);
			}
		}
	};
}

const renderPlaylists = function(response) {
	while (listOfPlaylists.childNodes.length > 2) {
    listOfPlaylists.removeChild(listOfPlaylists.lastChild);
	}
  for (let i = 1; i <= response.length; i++) {
    let playlistToAdd = document.createElement('p');
    playlistToAdd.innerText = response[i-1].title;
		playlistToAdd.setAttribute('title', response[i-1].pID);
		if (i % 2 === 0) {
			playlistToAdd.classList.add('dark');
		};
    playlistToAdd.addEventListener('click', function(){
			playlistActivator(i)
			setTracklist(response[i-1].pID);
    });
		if (i > 1) {
			let deleteButtonToAdd = document.createElement('span');
			deleteButtonToAdd.innerText = 'x';
			deleteButtonToAdd.classList.add('removePlaylist');
			deleteButtonToAdd.addEventListener('click', function(){
				removePlaylist(i);
			});
			playlistToAdd.appendChild(deleteButtonToAdd);
		};
    listOfPlaylists.appendChild(playlistToAdd);
  }
}

const playlistActivator = function(number) {
	let playlists = document.querySelectorAll('.listOfPlaylists p');
	for (let i = 0; i < playlists.length; i++) {
		playlists[i].classList.remove('active');
	}
	playlists[number].classList.add('active')
}

const setTracklist = function(playlistID = 0) {
	let url = '/playlist-tracks/';
	if (playlistID !== 0) {
		url += playlistID.toString();
	};
  ajaxGet(url, function (response) {
    console.log(response);
    if(response.length) {
      renderTracklist(response);
    } else {
      listOfTracks.innerHTML = '<h3>Nothing found :(</h3>';
    }
  });
}

const renderTracklist = function(response) {
  listOfTracks.innerHTML = '';
	tracksOfActivePlaylist = [];
  for (let i = 0; i < response.length; i++) {
		let trackToAdd = document.createElement('p');
    trackToAdd.innerText = i+1 + '.   ' + response[i].title + ' (' + response[i].artist + ')';
    let durationToAdd = document.createElement('span');
    let duration = timeConverter(response[i].duration);
    durationToAdd.innerText = duration;
		if (i % 2 === 0) {
			trackToAdd.classList.add('dark');
		};
		tracksOfActivePlaylist.push(response[i]);
		trackToAdd.addEventListener('click', function(){
      idOfActiveTrack = response[i].tID;
			console.log('idOfActiveTrack' + idOfActiveTrack);
			let tracks = document.querySelectorAll('.listOfTracks p');
			for (let i = 0; i < tracks.length; i++) {
				tracks[i].classList.remove('active');
			}
			trackToAdd.classList.add('active');
      setAudio(response[i]);
    });
    trackToAdd.appendChild(durationToAdd);
    listOfTracks.appendChild(trackToAdd);
  }
}

const setAudio = function(trackInfo) {
  console.log('audio started...');
	let url = 'assets/music/' + trackInfo.path;
	audio.setAttribute('src', url);
	trackTitle.innerText = trackInfo.title;
	artist.innerText = trackInfo.artist;
	addToFavStar.setAttribute("src", "/assets/img/star.svg")
}

ajaxGet('/playlists', renderPlaylists);
setTracklist();

// ajaxGet('/playlist-tracks', function(response) {
//   console.log('Progress with tracks');
// });
//
// ajaxGet('/playlist-tracks/:playlist_id=1', function(response) {
//   console.log('Progress with playlist 1');
// });

const timeConverter = function(duration) {
	let hours = '';
	let minutes = (Math.floor(duration / 60)).toString();
  let seconds = (Math.floor(duration % 60)).toString();
	if (seconds.length === 1) {
		seconds = '0' + seconds;
	}
	if (minutes >= 60) {
		hours = (Math.floor(minutes / 60)).toString() + ':';
		minutes = (Math.floor(duration % 60)).toString();
		if (minutes.length === 1) {
			minutes = '0' + minutes;
		}
	}
  let result = hours + minutes + ':' + seconds;
  return result;
}

const addPlaylistFunction = function() {
	addPlaylistDialog.classList.remove('invisible');
}

const addTrackFunction = function() {
	let targetPlaylists = listOfPlaylists.getElementsByTagName('p');
	select.innerHTML = '';
	for (let i = 1; i < targetPlaylists.length; i++) {
		let optionToAdd = document.createElement('option');
		optionToAdd.innerText = targetPlaylists[i].innerText.slice(0, -1);
		select.appendChild(optionToAdd);
	};
	addTrackDialog.classList.remove('invisible');
}

const addToFavFunction = function() {
	let message = {
    "tID": idOfActiveTrack
  };
	console.log(message);
	let url = '/playlist-tracks/1';
	ajaxPost(message, url, function(){
		console.log('ajaxPost ended');
	});
	addToFavStar.setAttribute("src", "/assets/img/star.png")
}

const playPrevTrack = function() {
	console.log('prev track loading...');
	console.log('id of last track: ' + idOfActiveTrack);
	console.log(tracksOfActivePlaylist);
	let trackInfo = null;
	for (let i = 1; i < tracksOfActivePlaylist.length; i++) {
		if (tracksOfActivePlaylist[i].tID === idOfActiveTrack) {
			console.log('equality found');
			trackInfo = tracksOfActivePlaylist[i-1];
		} else {
			trackInfo = tracksOfActivePlaylist[tracksOfActivePlaylist.length-1];
		}
	}
	console.log(trackInfo);
	setAudio(trackInfo);
}

const playNextTrack = function() {
	console.log('next track loading...');
	console.log('id of last track: ' + idOfActiveTrack);
	console.log(tracksOfActivePlaylist);
	let trackInfo = null;
	for (let i = 0; i < tracksOfActivePlaylist.length - 1; i++) {
		if (tracksOfActivePlaylist[i].tID === idOfActiveTrack) {
			console.log('equality found');
			trackInfo = tracksOfActivePlaylist[i+1];
		} else {
			trackInfo = tracksOfActivePlaylist[0];
		}
	}
	console.log(trackInfo);
	setAudio(trackInfo);
}

addPlaylist.addEventListener('click', addPlaylistFunction);
playlist0.addEventListener('click', function() {
	playlistActivator(0)
	setTracklist();
});
rewind.addEventListener('click', playPrevTrack);
pause.addEventListener('click', pause);
forward.addEventListener('click', playNextTrack);
shuffle.addEventListener('click', shuffle);
addTrack.addEventListener('click', addTrackFunction);
addToFav.addEventListener('click', addToFavFunction);
audio.addEventListener('ended', function(){
	console.log('ended happened');
	playNextTrack();
});

for (let i = 0; i < cancelButtons.length; i++) {
	cancelButtons[i].addEventListener('click', function() {
		addPlaylistDialog.classList.add('invisible');
		addTrackDialog.classList.add('invisible');
	});
}

submitPlaylistButton.addEventListener('click', function() {
	let playlistTitle = document.querySelector('.text');
	let message = {
    "title": playlistTitle.value
  };
	let url = '/playlists';
	ajaxPost(message, url, renderPlaylists);
	addPlaylistDialog.classList.add('invisible');
});

submitTrackButton.addEventListener('click', function() {
	let targetPlaylists = listOfPlaylists.getElementsByTagName('p');
	let playlist_id = null;
	for (let i = 1; i < targetPlaylists.length; i++) {
		if (targetPlaylists[i].textContent.slice(0, -1) === select.value) {
			playlist_id = targetPlaylists[i].title;
		};
	};
	let message = {
    "tID": idOfActiveTrack
  };
	let url = '/playlist-tracks/' + playlist_id;
	ajaxPost(message, url, function(){
		console.log('ajaxPost ended');
	});
	addTrackDialog.classList.add('invisible');
});
