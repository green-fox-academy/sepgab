'use strict';

// Create an Animal constructor
//
// Every animal has a hunger value, which is a number
// Every animal has a thirst value, which is a number
// when creating a new animal object these values are created with the default 50 value
// Every animal can eat() which decreases their hunger by one
// Every animal can drink() which decreases their thirst by one
// Every animal can play() which increases both by one
// Create a Farm constructor
//
// Every farm has list of Animals
// Every farm has slots which defines the number of free places for animals
// Every farm can breed() which creates a new animal if there's place for it
// Every farm can slaughter() which removes the least hungry animal

function animalConstructor() {
  this.hunger = 50;
  this.thirst = 50;
  this.eat = function() {
    return this.hunger--;
  }
  this.drink = function() {
    return this.thirst--;
  }
  this.play = function() {
    return this.thirst++, this.hunger++;
  }
}

function farmConstructor() {
  this.animalList = [];
  this.slots = 3;
  this.breed = function() {
    if (this.slots > 0) {
      var animal = new animalConstructor();
      this.animalList.push(animal);
      return this.slots--;
    }
  }
  this.slaughter = function() {
    if (this.animalList.length > 0) {
      var indexOfleastHungryAnimal = 0;
      for (var i = 0; i < this.animalList.length; i++) {
        console.log( i );
        if (this.animalList[i].hunger < this.animalList[indexOfleastHungryAnimal].hunger) {
          indexOfleastHungryAnimal = i;
        }
      }
      this.animalList.splice( indexOfleastHungryAnimal, 1 )
      return this.slots++;
    }
  }
}

let farm1 = new farmConstructor();
console.log( farm1 );
farm1.breed();
farm1.breed();
farm1.breed();
console.log( farm1.animalList );
farm1.animalList[1].eat();
console.log( farm1.animalList );
farm1.slaughter();
console.log( farm1.animalList );
