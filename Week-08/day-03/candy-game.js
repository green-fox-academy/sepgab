'use strict';

let candies = document.querySelector('.candies');
let lollypops = document.querySelector('.lollypops');
let showSpeed = document.querySelector('.speed');
let buttonCC = document.querySelector('.create-candies');
let buttonBL = document.querySelector('.buy-lollypops');
let buttonMCR = document.querySelector('.candy-machine');
let candyCounter = 0;
let lollypopCounter = 3;
let speed = 0;
let candyGen = 100;

let createCandies = function() {
  candyCounter += candyGen;
  display();
}

let buyLollypop = function() {
  if (candyCounter >= 100) {
    candyCounter -= 100;
    lollypopCounter++;
    speed = Math.max(parseInt(lollypopCounter/10), speed);
    display();
  }
}

let candyRainGen = function() {
  speed *= 10;
  display()
}

let display = function() {
  candies.innerText = candyCounter;
  let lollies = ''
  for (let i = 0; i < lollypopCounter; i++) {
    lollies += '🍭'
  }
  lollypops.innerText = lollies;
  showSpeed.innerText = speed;
}

let candyGenerator = function() {
  candyCounter += speed;
  display()
}

setInterval(candyGenerator, 1000)

buttonCC.addEventListener('click', createCandies);
buttonBL.addEventListener('click', buyLollypop);
buttonMCR.addEventListener('click', candyRainGen);
