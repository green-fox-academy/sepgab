'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer(name) {
  for (var i = 0; i < arguments.length; i++) {
    console.log( arguments[i] );
  }
}


printer("Tojas")
printer("Barbi", "CEO")
