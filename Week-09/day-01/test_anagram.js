'use strict';

var test = require('tape');
var anagram = require('./anagram');

test('anagramChecker test', function (t) {
    t.equal(anagram.anagramChecker('abba'), true);
    t.equal(anagram.anagramChecker('Abba'), false);
    t.equal(anagram.anagramChecker('Géza kék az ég'), false);
    t.equal(anagram.anagramChecker('Géza kék azéG'), true);
    t.end()
});
