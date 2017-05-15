'use strict';

var test = require('tape');
var count = require('./countletters');

test('Letter counter tester', function (t) {
    t.deepEqual(count.letterCounter('a'), { a: 1 } );
    t.deepEqual(count.letterCounter('aA'), { a: 1, A: 1 } );
    t.deepEqual(count.letterCounter('a is A'), { a: 1, ' ': 2, i: 1, s: 1, A: 1 } );
    t.deepEqual(count.letterCounter('a is 3'), { a: 1, ' ': 2, i: 1, s: 1, 3: 1 } );
    t.deepEqual(count.letterCounter('123'), { 1: 1, 2: 1, 3: 1 } );
    t.deepEqual(count.letterCounter(123), { 1: 1, 2: 1, 3: 1 } );
    t.end()
});
