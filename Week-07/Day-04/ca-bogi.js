var leftButton = document.querySelector('.left');
var rightButton = document.querySelector('.right');
var upButton = document.querySelector('.up');
var downButton = document.querySelector('.down');

var square = document.querySelector('.square');

var body = document.querySelector('body');

console.log(rightButton);

var posX = 0;
var posY = 0;

var posByClick = function() {
  return {
    UP: posY-50,
    DOWN: posY+50,
    LEFT: posX-50,
    RIGHT: posX+50
  }
}

function getDirection(e) {
  var target = e.target || e.srcElement;
  var direction = target.textContent;
  console.log(direction);
  return direction;
}

function changePos(e) {
  var direction = getDirection(e)

  if ( direction === 'UP' ) {
    if (checkWalls(direction)) {
      posY -= 50;
    }
  } else if (direction === 'DOWN' ) {
    if (checkWalls(direction)) {
      posY += 50;
    }
  } else if (direction === 'LEFT') {
    if (checkWalls(direction)) {
      posX -= 50;
    }
  } else if (direction === 'RIGHT') {
    if (checkWalls(direction)) {
      posX += 50;
    }
  }
  square.style.left = posX + 'px';
  square.style.top = posY + 'px';
  return [posX, posY];
}

function checkWalls(direction) {
  var pos = posByClick()
  if ( pos[direction] >= 0 && pos[direction] <= 450) {
    return true;
  }
  notification();
  return false;
}

function notification() {
  var notif = document.createElement('section');
  notif.textContent = 'Game Over';
  notif.style.fontsize = '30px';
  notif.style.color = 'blue';
  body.appendChild(notif);
}

rightButton.addEventListener('click', changePos);
leftButton.addEventListener('click', changePos);
upButton.addEventListener('click', changePos);
downButton.addEventListener('click', changePos);
