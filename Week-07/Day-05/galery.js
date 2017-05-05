'use strict';

var mainImage = document.querySelector('.main_image');
var thumbnails = document.querySelector('.thumbnails');
var leftButton = document.querySelector('.leftarrow');
var rightButton = document.querySelector('.rightarrow');
var index = 0;

function thumbnailFiller() {
  for (var i = 0; i < imageData.length; i++) {
    var imgToAdd = document.createElement('img');
    imgToAdd.style.maxWidth = '150px';
    imgToAdd.style.height = '100px';
    imgToAdd.style.margin = '5px';
    imgToAdd.style.border = '4px solid white';
    imgToAdd.style.borderRadius = '5px';
    imgToAdd.style.boxShadow = '0 20px 30px grey';
    imgToAdd.setAttribute('src', imageData[i].source);
    thumbnails.appendChild(imgToAdd);
  }
}

thumbnailFiller();

function imageFiller(num=0) {
  mainImage.setAttribute('src', imageData[num].source);
}

imageFiller(index);


function imageRight() {
  index += 1;
  if (index === imageData.length) {
    index = 0;
  }
  imageFiller(index);
  return index;
}

function imageLeft() {
  index -= 1;
  if (index === -1) {
    index = imageData.length-1;
  }
  imageFiller(index);
  return index;
}

leftButton.addEventListener('click', imageLeft);
rightButton.addEventListener('click', imageRight);
