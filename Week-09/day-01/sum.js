'use strict';


class operations {
  constructor(array) {
    this.array = array;
    this.summa = 0;
  }

  sum() {
    for (let i = 0; i < this.array.length; i++) {
      this.summa += this.array[i];
    }
    try {
      if (typeof this.summa !== 'number'){
        throw new Error('An element of the array is not a number');
      } else {
        return this.summa;
      }
    } catch(err) {
      return err.message
    }
  }
}

let op1 = new operations([1, 2, 3]);
console.log(op1.sum());

let op2 = new operations([1, 'string', 3]);
console.log(op2.sum());


let sum = function(array) {
  let summa = 0;
  array.forEach(function(el) {
    summa += el
  })
  return summa;
}

console.log(sum([1, 2, 3]));


module.exports = {
  sum: sum,
  operations: operations
}
