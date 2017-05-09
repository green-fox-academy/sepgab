'use strict'

let buttonUp = document.querySelector('.up');
let buttonDown = document.querySelector('.down');
let buttonAdd = document.querySelector('.add');
let buttonRemove = document.querySelector('.remove');
let floors = document.querySelector('.floors');
let peoples = document.querySelector('.people');
let elevatorIndex = 0;
let counter = 0;
let peopleOnFloors = [0,0,0,0,0,0,0,0,0,100]

let elevatorModel = {
  floorFiller: function() {
    for (let i = 0; i < 10; i++) {
      var floor = document.createElement('div');
      floors.appendChild(floor);
      var people = document.createElement('div');
      people.innerText = peopleOnFloors[i];
      peoples.appendChild(people);
    }
  },
  elevatorUp: function() {
    if (elevatorIndex < 9) {
      elevatorIndex++;
      elevatorView.display(elevatorIndex, counter);
    }
  },
  elevatorDown: function() {
    if (elevatorIndex > 0) {
      elevatorIndex--;
      elevatorView.display(elevatorIndex, counter);
    }
  },
  addPerson: function() {
    if (counter < 10 && peopleOnFloors[9-elevatorIndex] > 0) {
      counter++;
      let indexToUpdate = 10-elevatorIndex
      peopleOnFloors[indexToUpdate-1]--;
      let peopleToUpdate = document.querySelector('.people div:nth-child(' + indexToUpdate + ')');
      peopleToUpdate.innerText = peopleOnFloors[indexToUpdate-1];
      elevatorView.display(elevatorIndex, counter);
    }
  },
  removePerson: function() {
    if (counter > 0) {
      counter--;
      let indexToUpdate = 10-elevatorIndex
      peopleOnFloors[indexToUpdate-1]++;
      let peopleToUpdate = document.querySelector('.people div:nth-child(' + indexToUpdate + ')');
      peopleToUpdate.innerText = peopleOnFloors[indexToUpdate-1];
      elevatorView.display(elevatorIndex, counter);
    }
  }
}

let elevatorView = {
  display: function(floor, people) {
    let floorList = document.querySelectorAll('.floors div');
    let indexToGreen = 10-floor;
    floorList.forEach(function(el) {
      if (el.style.backgroundColor = 'green') {
        el.style.backgroundColor = 'white';
        el.innerText = ''
      }
    });
    let FloorToGreen = document.querySelector('.floors div:nth-child(' + indexToGreen + ')')
    FloorToGreen.style.backgroundColor = 'green';
    FloorToGreen.innerText = people;
  }
}

let elevatorController = {
  init: function() {
    elevatorModel.floorFiller();
    elevatorView.display(elevatorIndex, counter);
    buttonUp.addEventListener('click', elevatorModel.elevatorUp);
    buttonDown.addEventListener('click', elevatorModel.elevatorDown);
    buttonAdd.addEventListener('click', elevatorModel.addPerson);
    buttonRemove.addEventListener('click', elevatorModel.removePerson);
  }
}

elevatorController.init();
