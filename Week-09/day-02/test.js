var http = require('http');

// var server = http.createServer(function(req, res) {
//   console.log('Request was made: ' + req.url);
//   res.writeHead(200, {'Content-Type': 'text/plain'});
//   res.end('Hey ninjaaas');
// });

var server = http.createServer(function(req, res) {
  console.log('Request was made: ' + req.url);
  res.writeHead(200, {'Content-Type': 'application/JSON'});
  var myObj = {
    name: 'Ryu',
    age: 29,
    job: 'Ninja'
  };
  res.end(JSON.stringify(myObj));
});

server.listen(3000, '127.0.0.1');
console.log('yo dawgs, now listening to port 3000.');
