'use strict';

var express = require('express');
var five = require('five')

var app = express();

app.get('/', function(req, res){
  console.log( req.url );
  res.send('<a href="#">Ez itt a főoldal</a>');
});

app.get('/valami', function(req, res){
  res.send({
    name: 'Balozska',
    age: 12,
    gender: 'male'
  });
});

app.get('/five/:lang', function(req, res){
  var lang = req.params.lang;
  var fiveFunct = five[lang] ;
  res.send(fiveFunct());
});

app.listen(3000);
