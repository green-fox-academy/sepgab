'use strict';

var test = require('tape');
var fibo = require('./fibonacci');

test('Fibonacci index tester', function (t) {
    t.equal(fibo.getFibonacci(6), 8);
    t.equal(fibo.getFibonacci(1), 1);
    t.equal(fibo.getFibonacci(2), 1);
    t.equal(fibo.getFibonacci(0), 'Incorrect input');
    t.equal(fibo.getFibonacci(null), 'Incorrect input');
    t.equal(fibo.getFibonacci('string'), 'Incorrect input');
    t.equal(fibo.getFibonacci(0.5), 'Incorrect input');
    t.equal(fibo.getFibonacci(0, 1), 'Incorrect input');
    t.end()
});
