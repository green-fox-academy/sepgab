'use strict';

var test = require('tape');
var sumFile = require('./sum');

test('Sum tester', function (t) {
    t.equal(sumFile.sum([1, 2, 3]), 6);
    t.end()
});

test('Sum object tester', function (t) {
    let var1 = new sumFile.operations([1, 2, 3]);
    t.equal(var1.sum(), 6);

    let var2 = new sumFile.operations([]);
    t.equal(var2.sum(), 0);

    let var3 = new sumFile.operations([null]);
    t.equal(var3.sum(), 0);

    let var4 = new sumFile.operations([2]);
    t.equal(var4.sum(), 2);

    let var5 = new sumFile.operations(['string']);
    t.equal(var5.sum(), 'An element of the array is not a number');

    t.end()
});
