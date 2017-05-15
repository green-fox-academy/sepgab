'use strict';

// Adds a and b, returns as result
const addNumbers = function(a, b) {
  let summa = a + b;
  if (typeof summa !== 'number'){
    throw new Error('Invalid value');
  } else {
    return summa;
  }
}

// Returns the highest value from the three given params
const maxOfThree = function(a, b, c) {
  if (typeof a !== 'number' || typeof b !== 'number' || typeof c !== 'number') {
    throw new Error('Invalid value');
  } else {
    if (a >= b && a >= c) {
      return a;
    } else if (b >= a && b >= c) {
      return b;
    } else if (c >= a && c >= b) {
      return c;
    }
  }
}

//Returns the median value of a list given as param
const median = function(pool){
  try {
    pool.forEach(function(el) {
      if (typeof el  !== 'number') {
        throw new Error('Invalid value');
      }
    });
    let sortedPool = pool.sort();
    let half = Math.floor(pool.length/2);
    if (pool.length % 2) {
      return sortedPool[half];
    } else {
      return (sortedPool[half-1] + sortedPool[half]) / 2;
    }
  } catch(err) {
    return err.message
  }


}

// Returns true if the param is a vovel
const isVovel = function(char){
  if (char.length !== 1) {
    return 'Please, give me one character'
  } else {
    return 'aeiouéáőűöüóí'.indexOf(char) >= 0
  }
}

// Create a method that translates hungarian into the teve language
const translate = function(hungarian) {
  try {
    if (typeof hungarian !== 'string') {
      throw new Error('Invalid value');
    }
    let text = hungarian.toString().split('');
    let teve = '';
    text.forEach(function(char){
      if (isVovel(char)){
        teve += char + 'v'+ char;
      } else {
        teve += char;
      }
    });
    return teve;
  } catch(err) {
    return err.message
  }
}

module.exports = {
  addNumbers: addNumbers,
  maxOfThree: maxOfThree,
  median: median,
  isVovel: isVovel,
  translate: translate
}
