'use strict';
// Saturn is missing from the planetList
// Insert it into the correct position
// bonus for using some built in methods

var planetList = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"];


planetList[7] = planetList[6];
planetList[6] = planetList[5];
planetList[5] = 'Saturn';

console.log(planetList);
