'use strict';

let audio = document.querySelector('audio');
// let play = document.querySelector('play');
// let pause = document.querySelector('pause');


audio.addEventListener('loadstart', function() {
  console.log('loadstart happened');
});
audio.addEventListener('play', function() {
  console.log('play happened');
});
audio.addEventListener('ended', function() {
  console.log('ended happened');
});
audio.addEventListener('progress', function() {
  console.log('progress happened');
});
