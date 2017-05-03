'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs:
//  - how many candies they have on average

function candyMoreThan4(list) {
  var listOfOwners = [];
  list.forEach(function(el) {
    if (el.candies > 4) {
      listOfOwners.push(el.name);
    }
  })
  console.log( 'Who has more than 4 candies: ' + listOfOwners);
}

function averageCandies(list) {
  var sum = 0;
  list.forEach(function(el) {
    sum += el.candies;
  })
  console.log( sum / list.length );
}

candyMoreThan4(students);

averageCandies(students);
