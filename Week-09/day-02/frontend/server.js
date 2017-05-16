'use strict';

var express = require('express');
var bodyParser = require('body-parser')

var app = express();

app.use(bodyParser.json());

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
  app.use('/assets/', express.static('assets'));
});

app.get('/doubling', function(req, res){
  var number = req.query.input
  if (number !== undefined) {
    res.send({
      "received": number,
      "result": number*2
    });
  } else {
    res.send({
      "error": "Please provide an input!"
    });
  }
});

app.get('/greeter', function(req, res){
  var name = req.query.name;
  var title = req.query.title;
  if (name === undefined) {
    res.send({
      error: "Please provide a name!"
    });
  } else if (title === undefined) {
    res.send({
      error: "Please provide a title!"
    });
  } else {
    res.send({
      welcome_message: "Oh, hi there " + name + ", my dear " + title + "!"
    });
  }
});

app.get('/appenda/:appendable', function (req, res){
  var appendable = req.params.appendable;
  if (appendable === undefined) {
    res.status(404).send('Not found');
  } else {
    var appended = appendable + 'a';
    res.send({
      'appended': appended
    });
  }
});

app.post('/dountil/:what', function (req, res){
  var what = req.params.what;
  var until = req.body.until;
  console.log( req.body );

  function sum(number) {
    let answer = 0;
    for (let i = 0; i <= number; i++) {
      answer += i;
    }
    return answer
  }

  function factor(number) {
    let answer = 1;
    for (let i = 1; i <= number; i++) {
      answer *= i;
    }
    return answer
  }

  if (what === 'sum') {
    res.send({
      "result": sum(until)
    })
  } else if (what === 'factor') {
    res.send({
      "result": factor(until)
    })
  }
})




app.listen(8080, function(){
  console.log( 'Server is running');
});
