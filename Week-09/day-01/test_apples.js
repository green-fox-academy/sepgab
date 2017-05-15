'use strict';
var test = require('tape');
var apples = require('./apples');

test('Apple tester', function (t) {
    t.equal( getApple(), 'Apple');
    t.end()
});
