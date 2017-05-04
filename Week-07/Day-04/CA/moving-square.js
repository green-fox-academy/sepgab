var leftButton = document.querySelector('.left');
var rightButton = document.querySelector('.right');
var downButton = document.querySelector('.down');
var upButton = document.querySelector('.up');

var clearButton = document.querySelector('.clear');

var square = document.querySelector('.square');

var body = document.querySelector('body');

console.log(rightButton);

var posX = 0;
var posY = 0;

var colorIndex = 0;

var posByClick = function () {
  return {
    UP: posY - 50,
    DOWN: posY + 50,
    LEFT: posX - 50,
    RIGHT: posX + 50
  }
}

function getDirection(e) {
  var target = e.target || e.srcElement;
  var direction = target.textContent;
  return direction;
}

function changePos(e) {
  var direction = getDirection(e);
  console.log(direction);
  if ( direction === 'UP') {
    if(checkWalls(direction)) {
      posY = posY - 50;
    }
  } else if ( direction === 'DOWN') {
    if(checkWalls(direction)) {
      posY = posY + 50;
    }
  } else if ( direction === 'LEFT') {
    if (checkWalls(direction)) {
      posX = posX - 50;
    }
  } else if ( direction === 'RIGHT') {
    if ( checkWalls(direction)) {
      posX = posX + 50;
    }
  }
  square.style.top = posY + "px";
  square.style.left = posX + "px";
  return [posX, posY];
}


function checkWalls(direction) {
  var pos = posByClick();
  if ( pos[direction] >= 0 && pos[direction] <= 450) {
    return true;
  }
  notification();
  return false;
}

function notification() {
  var notif = document.createElement('section');
  notif.textContent = 'Game Over';
  notif.style.fontSize = '30px';
  notif.style.color = colors[colorIndex];
  colorIndex++;
  body.appendChild(notif);
}

function clearNotif() {
  var sections = document.querySelectorAll('section');
  console.log(sections);
  console.log(sections[0]);
  for (var i = 0; i < sections.length; i++) {
    // console.log(element);
    body.removeChild(sections[i]);
  }
}

rightButton.addEventListener('click', changePos);
leftButton.addEventListener('click', changePos);
upButton.addEventListener('click', changePos);
downButton.addEventListener('click', changePos);
clearButton.addEventListener('click', clearNotif);
