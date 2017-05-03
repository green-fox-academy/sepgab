'use strict';

var beka = 1;

function hello(name='MySchool') {
  console.log(beka);
  beka = name;
  return name + ' => ' + name;
}
hello('Tibi');
console.log( beka );



function hello() {
  console.log(arguments.length);
  console.log('Hello Mr.', arguments[0] );
}

function getName() {
  return 'Bond';
}

hello('Bond')


function hello2( who ) {
  console.log('Hello Mr. ', who() )
}

hello2( function () {
  return 'Bond';
})



console.log( parseInt( '4.5kjn') );



var myColl = ['hello', 'bello', [1, 2, 3]]

console.log( myColl.length )

for (var i = 0; i < myColl.length; i++) {
  console.log( 'YO', myColl[i]);
}

myColl.push('hi')
console.log(myColl)

console.log( myColl.pop() )
console.log(myColl)

console.log( myColl.shift() )
console.log(myColl)

console.log( myColl.unshift('First') )
console.log(myColl)

console.log( myColl.indexOf('bello') )
console.log(myColl)

console.log( myColl.indexOf('First') )
console.log(myColl)

console.log( myColl.unshift('blah') )
console.log(myColl)

console.log( myColl.slice(1,3) )
console.log(myColl)

myColl.forEach(function(el) {
  console.log(el)
})

myColl.forEach(function(el, i, fullArray) {
  console.log(el, i, fullArray)
})

var res = myColl.forEach(function(el, i) {
  myColl[i] = el*2;
})
console.log(res);


var myColl = [1, 2, 3, 4]
var result = myColl.map(function(el, i){
  return el * 2;
})
console.log(result)

console.log(myColl)
var result = myColl.filter(function(el, i){
  return i%2;
})
console.log(result)




var str = 'this is a string';

console.log(str.indexOf('tibi'));
console.log(str.indexOf('a string'));

console.log( str.replace('a', 'your') );

console.log( str.split('') );
console.log( str.split('').join('>') );

var str = 'this is a string';

console.log(str.substr(0,5));
console.log(str.substr(-6));

var str = '   this is a    string        ';

console.log( str.trim())

var str = 'this is a string';

console.log(str.endsWith('string'));
console.log(str.startsWith('that'));




var car = {
  type: 'mazda',
  year: 1999,
  colors: {
    roof: 'red',
    doors: 'green'
  }
}

console.log( car )
console.log( car.year )
console.log( car.year.toString() )
console.log( car.colors.roof )

console.log( Object, String )
console.log( Object.keys(car) )
// console.log( Object.values(car) ) later...

var galery = []
galery.push( {item: 'first pic'} )
galery.push({item: 'second pic'})
galery.item = 'Third'

console.log( galery )
