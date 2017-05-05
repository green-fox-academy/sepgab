'use strict';

var mainImage = document.querySelector('.main_image');
var title = document.querySelector('.title')
var descr = document.querySelector('.descr')
var thumbnails = document.querySelector('.thumbnails');
var leftButton = document.querySelector('.leftarrow');
var rightButton = document.querySelector('.rightarrow');
var index = 0;

function thumbnailFiller() {
  for (let i = 0; i < imageData.length; i++) {
    var imgToAdd = document.createElement('img');
    imgToAdd.setAttribute('src', imageData[i].source);
    imgToAdd.addEventListener('click', function(){mainImage.setAttribute('src', imageData[i].source); title.innerText = imageData[i].title; descr.textContent = imageData[i].description; index = i; return index});
    thumbnails.appendChild(imgToAdd);
  }
}

thumbnailFiller();

function imageFiller(num=0) {
  mainImage.setAttribute('src', imageData[num].source);
  title.innerText = imageData[index].title;
  descr.textContent = imageData[index].description;
  borderer();
}

imageFiller(index);

function borderer() {
  var imageList = document.querySelectorAll('.thumbnails img')
  console.log( imageList );
  imageList.forEach(function(el) {
    el.style.borderColor = 'white';
  })

  console.log( index+1 );
  var childToBlack = document.querySelector('.thumbnails img:nth-child(' + index+1 + ')')
  childToBlack.style.borderColor = 'black';
}


function imageRight() {
  index++;
  if (index === imageData.length) {
    index = 0;
  }
  imageFiller(index);
  borderer();
  return index;
}

function imageLeft() {
  index--;
  if (index === -1) {
    index = imageData.length-1;
  }
  imageFiller(index);
  borderer();
  return index;
}

leftButton.addEventListener('click', imageLeft);
rightButton.addEventListener('click', imageRight);
