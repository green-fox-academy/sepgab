'use strict';

var imageData = [
  {
    source: 'images\image1.jpg',
    title: 'Image1',
    description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    source: 'images\image2.jpg',
    title: 'Image2',
    description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    source: 'images\image3.jpg',
    title: 'Image3',
    description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    source: 'images\image4.jpg',
    title: 'Image4',
    description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    source: 'images\image5.jpg',
    title: 'Image5',
    description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  }
]


var thumbnails = document.querySelector('.thumbnails');

for (var i = 0; i < imageData.length; i++) {
  var imgToAdd = document.createElement('img');
  imgToAdd.style.width = '150px';
  imgToAdd.style.height = '100px';
  imgToAdd.setAttribute('src', imageData[i].source);
  thumbnails.appendChild(imgToAdd);
}
