// Create a Sharpie constructor
//
// We should know about each sharpie their color (which should be a string), width (which will be a floating point number), inkAmount (another floating point number)
// When creating one, we need to specify the color and the width
// Every sharpie is created with a default 100 as inkAmount
// We can use() the sharpie objects
// which decreases inkAmount by the width

'use strict';

function sharpieMaker(color, width) {
  this.color = color;
  this.width = width;
  this.inkAmount = 100,
  this.use = function() {
    return this.inkAmount -= this.width;
  }
}

var sharpie1 = new sharpieMaker('black', 5);
console.log( sharpie1 );
sharpie1.use();
console.log( sharpie1 );

var sharpie2 = new sharpieMaker('black', 5);
console.log( sharpie2 );
sharpie2.use();
console.log( sharpie2 );
