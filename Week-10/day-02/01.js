'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(talk) {
  this.talk = talk;
}

Animal.prototype.say = function() {
  console.log( this.talk );
}

var dog = new Animal('WOOUFF');
dog.say();
