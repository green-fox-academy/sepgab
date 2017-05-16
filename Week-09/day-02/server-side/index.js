'use strict';

var http = require('http');
var five = require('five');

console.log(five.klingon());

var server = http.createServer(handleRequest);

function handleRequest(request, response) {
  console.log( request );
  response.end('hellooo listener');
}

server.listen(3000);
