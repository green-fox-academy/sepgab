'use strict';

var mainImage = document.querySelector('.main_image');
var thumbnails = document.querySelector('.thumbnails');

function thumbnailFiller() {
  for (var i = 0; i < imageData.length; i++) {
    var imgToAdd = document.createElement('img');
    imgToAdd.style.maxWidth = '150px';
    imgToAdd.style.height = '100px';
    imgToAdd.style.margin = '5px';
    imgToAdd.setAttribute('src', imageData[i].source);
    thumbnails.appendChild(imgToAdd);
  }
}

thumbnailFiller();

function imageFiller(index=0) {
  mainImage.setAttribute('src', imageData[index].source);
}

imageFiller();
