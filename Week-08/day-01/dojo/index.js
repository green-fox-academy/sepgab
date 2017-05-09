'use strict';
var test = require('tape');

function validate() {
  return false;
}

test('Validator test', function (t) {
    t.equal( validate(), false, 'existential text');
    t.deepEqual( [1,2,3], [1,2,3]);
    t.equal(1,1);
    t.end()
});
