'use strict';

var test = require('tape');
var apples = require('./apples');

test('Apple tester', function (t) {
    t.equal( apples.getApple(), 'Apple');
    t.end()
});
